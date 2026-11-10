"""Validate build inputs and the packaged variant without loading the synthesizer."""
from __future__ import annotations
import argparse
import ast
import gettext
import hashlib
from html.parser import HTMLParser
import io
from pathlib import Path, PurePosixPath
import runpy
import sys
import zipfile
import polib

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def require(condition, message):
    if not condition:
        raise ValueError(message)


class HelpParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.lang = None; self.headings = []; self.links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html": self.lang = attrs.get("lang")
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}: self.headings.append(int(tag[1]))
        if tag in {"a", "link"}: self.links.append(attrs.get("href", ""))


def source_checks(build):
    messages = set()
    for pattern in build["i18nSources"]:
        for path in ROOT.glob(pattern):
            tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
            for node in ast.walk(tree):
                if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                        and node.func.id == "_" and node.args
                        and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str)):
                    messages.add(node.args[0].value)
    pot = polib.pofile(str(ROOT / "vocalizer_automotive_driver.pot"))
    require(messages == {entry.msgid for entry in pot if not entry.obsolete}, "POT differs from sources; run uv run scons pot")
    catalogs = {}
    fallback = 0
    for path in sorted(ROOT.glob("addon/locale/*/LC_MESSAGES/nvda.po")):
        catalog = polib.pofile(str(path)); lang = path.parents[1].name
        if lang in {"pl", "sk"}:
            missing = [msg for msg in messages if not catalog.find(msg) or not catalog.find(msg).translated()]
            require(not missing, f"{lang}: missing current translations: {missing}")
        fallback += sum(1 for msg in messages if not catalog.find(msg) or not catalog.find(msg).translated())
        catalogs[lang] = catalog
    require(len(catalogs) == 25, "Expected the 25 existing translation catalogs")
    require({"pl", "sk"} <= catalogs.keys(), "Missing maintained translations")
    for path in [ROOT / "sconstruct", *ROOT.glob("tools/*.py")]:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    print(f"Sources OK: {len(messages)} messages, {len(catalogs)} locales; existing English fallbacks: {fallback}")
    return catalogs


def package_checks(path, build, catalogs):
    info = build["addon_info"]
    with zipfile.ZipFile(path) as bundle:
        require(bundle.testzip() is None, "Corrupt archive")
        names = bundle.namelist(); require(len(names) == len(set(names)), "Duplicate archive entries")
        required = {"manifest.ini", "gpl.txt", "NOTICE.txt", "doc/style.css"}
        required |= {p.removeprefix("addon/") for p in build["runtimeHashes"]}
        required |= {f"doc/{lang}/readme.html" for lang in ["en", "pl", "sk"]}
        for lang in catalogs:
            required |= {f"locale/{lang}/manifest.ini", f"locale/{lang}/LC_MESSAGES/nvda.mo"}
        require(required <= set(names), f"Missing package files: {required - set(names)}")
        for name in names:
            p = PurePosixPath(name); low = name.lower()
            require(not p.is_absolute() and ".." not in p.parts and "\\" not in name, f"Unsafe path: {name}")
            require(not name.startswith("addon/") and "__pycache__" not in p.parts, f"Unexpected path: {name}")
            require(p.suffix.lower() not in {".pyc", ".pyo", ".po", ".pot", ".md", ".ps1"}, f"Source/cache in package: {name}")
            require(p.name.lower() != "vocalizer_license.ini", "User license included in package")
            require(not p.name.lower().startswith("nuan_platform.dll") or p.name.lower() == "nuan_platform.dll", f"Backup DLL in package: {name}")
            if p.suffix == ".py":
                require(bundle.read(name) == (ROOT / "addon" / name).read_bytes(), f"Changed Python payload: {name}")
        for source, checksum in build["runtimeHashes"].items():
            require(hashlib.sha256(bundle.read(source.removeprefix("addon/"))).hexdigest() == checksum, f"Runtime asset mismatch: {source}")
        for source in (ROOT / "addon").rglob("*.py"):
            require(source.relative_to(ROOT / "addon").as_posix() in names, f"Missing runtime source: {source}")
        if build["variant"].startswith("legacy"):
            require("synthDrivers/vocalizerAutomotive32.py" not in names, "Bridge in legacy package")
        else:
            require("synthDrivers/vocalizerAutomotive32.py" in names, "Missing bridge")
        if build["variant"] == "brokered-audio":
            require("synthDrivers/_automotiveBrokeredProxy32.py" in names, "Missing brokered proxy")
        manifest = bundle.read("manifest.ini").decode("utf-8")
        for field, key in [("name", "addon_name"), ("version", "addon_version"), ("url", "addon_url"),
                           ("minimumNVDAVersion", "addon_minimumNVDAVersion"), ("lastTestedNVDAVersion", "addon_lastTestedNVDAVersion")]:
            require(f"{field} = {info[key]}" in manifest.splitlines(), f"Manifest mismatch: {field}")
        for lang, catalog in catalogs.items():
            mo = gettext.GNUTranslations(io.BytesIO(bundle.read(f"locale/{lang}/LC_MESSAGES/nvda.mo")))
            for entry in catalog:
                if entry.translated() and not entry.obsolete and not entry.msgid_plural:
                    require(mo.gettext(entry.msgid) == entry.msgstr, f"{lang}: stale MO: {entry.msgid!r}")
            translated = bundle.read(f"locale/{lang}/manifest.ini").decode("utf-8")
            description = mo.gettext(info["addon_description"])
            require(f'description = """{description}"""' in translated, f"{lang}: stale description")
        for lang in ["en", "pl", "sk"]:
            parser = HelpParser(); parser.feed(bundle.read(f"doc/{lang}/readme.html").decode("utf-8"))
            require(parser.lang == lang and parser.headings.count(1) == 1 and len(parser.headings) > 2, f"{lang}: invalid help structure")
            require(all(b <= a + 1 for a, b in zip(parser.headings, parser.headings[1:])), f"{lang}: skipped heading")
    print(f"Package OK: {path.name} ({len(names)} files), variant={build['variant']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", action="store_true")
    parser.add_argument("--output-directory", type=Path, default=ROOT / "dist")
    parser.add_argument("--write-checksum", action="store_true")
    args = parser.parse_args()
    if args.write_checksum and not args.package: parser.error("--write-checksum requires --package")
    build = runpy.run_path(str(ROOT / "buildVars.py")); catalogs = source_checks(build)
    if args.package:
        info = build["addon_info"]; package = args.output_directory / f'{info["addon_name"]}-{info["addon_version"]}.nvda-addon'
        package_checks(package, build, catalogs)
        if args.write_checksum:
            checksum = hashlib.sha256(package.read_bytes()).hexdigest()
            package.with_suffix(package.suffix + ".sha256").write_text(f"{checksum}  {package.name}\n", encoding="utf-8")
            print(f"SHA-256 written: {checksum}")


if __name__ == "__main__":
    try: main()
    except (ValueError, OSError, zipfile.BadZipFile) as error: sys.exit(f"Validation failed: {error}")

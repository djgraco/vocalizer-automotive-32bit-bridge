"""Restore the legacy branch's published engine assets from existing Git objects."""
import hashlib
from pathlib import Path
import subprocess


def restore_runtime(target: Path, asset: dict) -> None:
    root = Path(__file__).resolve().parent.parent
    if target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest() == asset["sha256"]:
        return
    try:
        data = subprocess.check_output(["git", "cat-file", "blob", asset["blob"]], cwd=root, stderr=subprocess.PIPE)
    except (OSError, subprocess.CalledProcessError) as error:
        raise RuntimeError(
            "Legacy runtime assets are not in this checkout's Git objects. Use a full clone "
            "of the project (all three branches); for a shallow clone fetch the full history. "
            "No license or engine is downloaded automatically."
        ) from error
    if hashlib.sha256(data).hexdigest() != asset["sha256"]:
        raise ValueError(f"Unexpected runtime contents for {target.name}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)

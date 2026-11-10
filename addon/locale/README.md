# Translation workflow

The root `vocalizer_automotive_driver.pot` is generated from runtime source and
`buildVars.py` using `uv run --locked scons pot`. Update a PO file from that
template with Poedit or msgmerge, then build with `uv run --locked scons`.

PO files live at `addon/locale/<language>/LC_MESSAGES/nvda.po`. The build
compiles MO files and generates localized manifests from the summary and
description messages in those same catalogs. Do not edit generated manifests
or MO files. Existing manifest translations have been migrated without rewording.

The 25 historical locales are retained. Existing untranslated messages in
unmaintained catalogs continue falling back to English. Polish and Slovak
coverage is checked for current source messages. Preserve placeholders such
as `{error}`, `{driverVersion}`, `{licenseInfo}` and menu accelerator markers.

Help sources are Markdown in `addon/doc/<language>/readme.md`; the build
generates HTML. Match the interface's actual translated labels. Validate the
package following [building instructions](../../docs/building.md).

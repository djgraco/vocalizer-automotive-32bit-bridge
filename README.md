# Vocalizer Automotive 32-bit Bridge for NVDA

[Polski](README.pl.md) | [Slovenčina](README.sk.md) | English

This project adapts the legacy 32-bit Nuance Vocalizer Automotive 5.5 NVDA
driver for both 32-bit and 64-bit NVDA.

On 32-bit NVDA, the original Automotive driver is loaded directly. On
64-bit NVDA, the bridge runs it in NVDA's dedicated 32-bit synthesizer host.
The method used to route speech audio depends on the installed variant:
standard or brokered audio.

## Important

The package does **not** include separate Vocalizer voice add-ons or the
user-specific `vocalizer_license.ini` file. A valid license is still required
by the runtime and must be imported separately.

This fork is maintained independently. Report issues through this repository and do not direct support requests to vendors or maintainers of the original components. The original Vocalizer Automotive 5.5 project is no longer officially developed or supported. The original add-on author is not responsible for this independent fork, any modifications made to it, or technical support.

## Installation

1. Install the public `.nvda-addon` file from the GitHub Releases page, or
   copy this repository into the NVDA add-ons directory.
2. The package already contains the required Automotive runtime components.
3. Install your own Vocalizer Automotive voice add-ons separately. Their
   directories normally begin with `vocalizer-voice-`.
4. Start NVDA and open:

   `NVDA menu > Vocalizer Automotive > Enter License`

   The license is copied to:

   `%APPDATA%\nvda\vocalizer_license.ini`

5. Restart NVDA and select the driver matching your NVDA architecture:

   - 32-bit NVDA: `vocalizerAutomotive`
   - 64-bit NVDA: `vocalizerAutomotive32`

## Audio Processing

The standard variant uses the classic NVDA compatibility bridge on 64-bit
NVDA. On 32-bit NVDA, Automotive uses its native direct path. Sonic Pitch does
not work with the standard variant.

For audio routed through the main NVDA process, native NVDA audio ducking and
Sonic Pitch compatibility on supported 64-bit NVDA versions, install the
brokered-audio variant.

## Available Variants

- **Standard variant:** uses the classic compatibility bridge on 64-bit NVDA
  2026.1 and newer, and the native direct path on 32-bit NVDA.
- **Brokered-audio variant:** routes speech audio through the main NVDA process
  on 64-bit NVDA 2026.2 and newer, and uses the native direct path on 32-bit
  NVDA.

Install only one variant at a time.

## Automatic Language Switching

The menu contains **Automatic Language Switching Settings**. The dialog
detects installed Automotive voice resources from their `.hdr` metadata and
stores the selected voice mapping in:

`%APPDATA%\nvda\vocalizer.ini`

The add-on interface includes the original translations for these locales:
`an`, `ar`, `da`, `de`, `el`, `es`, `fi`, `fr`, `gl`, `hr`, `hu`, `it`, `ja`,
`ko`, `nb_NO`, `ne`, `nl`, `pl`, `pt_BR`, `pt_PT`, `ru`, `sk`, `sl`, `tr` and
`zh_CN`. HTML documentation is available in English, Polish and Slovak.
NVDA uses the language selected in its general settings.

The reusable translation template is available at
`locale/vocalizer_automotive_driver.pot`.

## Runtime Check

Run:

```powershell
.\tools\Check-VocalizerAutomotiveRuntime.ps1
```

The script reports required runtime files, detected voice add-ons and the
separate license file. It does not download or include a license.

## Building

To build the complete add-on package:

```powershell
.\tools\Build-PublicAddon.ps1
```

The package is written to `dist` and includes the runtime files stored in the
repository. The build always excludes `vocalizer_license.ini`.

## License

The NVDA driver and bridge source is distributed under GPL-2.0 as described
in [LICENSE](LICENSE) and [gpl.txt](gpl.txt). The included runtime components
are separate runtime files included with this fork. Voice add-ons and
user-specific license files are not included.

# Vocalizer Automotive 5.5 Driver

This add-on adapts the legacy 32-bit Nuance Vocalizer Automotive 5.5 driver for both 32-bit and 64-bit NVDA.

On 32-bit NVDA, the original Automotive driver is loaded directly. On 64-bit NVDA, the bridge runs it in NVDA's dedicated 32-bit synthesizer host. The method used to route speech audio depends on the installed variant: standard or brokered audio.

## Installation

1. Install the add-on.
2. Install your voice add-ons separately.
3. Use **NVDA menu > Vocalizer Automotive** to enter the license and configure automatic language switching.
4. Restart NVDA and select `vocalizerAutomotive` on 32-bit NVDA, or `vocalizerAutomotive32` on 64-bit NVDA.

The license file is not included in the package and must be imported from your own licensed copy.

## Audio processing

The standard variant uses the classic NVDA compatibility bridge on 64-bit NVDA. On 32-bit NVDA, Automotive uses its native direct path. Sonic Pitch does not work with the standard variant.

For audio routed through the main NVDA process, native NVDA audio ducking and Sonic Pitch compatibility on supported 64-bit NVDA versions, install the brokered-audio variant.

## Available variants

- **Standard variant:** uses the classic compatibility bridge on 64-bit NVDA 2026.1 and newer, and the native direct path on 32-bit NVDA.
- **Brokered-audio variant:** routes speech audio through the main NVDA process on 64-bit NVDA 2026.2 and newer, and uses the native direct path on 32-bit NVDA.

Install only one variant at a time.

## Automatic language switching

The settings dialog detects installed voices from their `.hdr` metadata and stores the selected mapping in `%APPDATA%\nvda\vocalizer.ini`.

## Translations

The add-on interface includes the original translations for locales `an`, `ar`, `da`, `de`, `el`, `es`, `fi`, `fr`, `gl`, `hr`, `hu`, `it`, `ja`, `ko`, `nb_NO`, `ne`, `nl`, `pl`, `pt_BR`, `pt_PT`, `ru`, `sk`, `sl`, `tr` and `zh_CN`. HTML documentation is available in English, Polish and Slovak.

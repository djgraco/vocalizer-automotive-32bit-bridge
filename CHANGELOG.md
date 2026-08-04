# Changelog

All notable changes to this project are documented in this file.

## [2.2.0] - 2026-08-03

### Fixed

* Fixed the brokered 32-bit bridge lifecycle when changing the audio output device, preventing the NVDA Settings dialog from becoming unavailable after repeated changes.
* Fixed cleanup of the RPyC pipe streams used by brokered audio, eliminating repeated `Bad file descriptor` errors.
* Fixed audio output device selection on NVDA 2025.1 and later by reading `audio.outputDevice`, with a fallback to the legacy `speech.outputDevice` setting.
* Hardened cleanup after partial 32-bit host initialization failures, avoiding invalid process-handle polling.

## [2.1.7] final - 2026-08-03

### Fixed

* Fixed audio output device selection on NVDA 2025.1 and later by reading `audio.outputDevice`, with a fallback to the legacy `speech.outputDevice` setting.

## [2.2.0] - 2026-07-27

### Changed

* Changed the behavior of the **Download More Voices** menu item. It now opens the original download redirection used by the legacy Vocalizer Automotive add-on.
* Updated the add-on manifest for the brokered-audio release.

## [2.1.7] - 2026-07-27

### Changed

* Changed the behavior of the **Download More Voices** menu item. It now opens the original download redirection used by the legacy Vocalizer Automotive add-on.
* Updated the add-on manifest for the classic bridge release.

# Build metadata only. Add-on runtime source is unchanged.
from site_scons.site_tools.NVDATool.typings import AddonInfo
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
	addon_name='vocalizer_automotive_driver',
	addon_summary=_('Vocalizer Automotive 5.5 Driver'),
	addon_description=_('Driver and interface for Nuance Vocalizer Automotive 5.5.\nTo use it, you must have a valid license and install, at least, one voice downloadable from https://vocalizer-nvda.com/old/en/downloads.htm'),
	addon_version='2.2.0-2026-08-25',
	addon_changelog='',
	addon_author='Tiflotecnia, LDA. modified by DJ Graco & Kazek5p',
	addon_url='https://github.com/djgraco/vocalizer-automotive-32bit-bridge',
	addon_sourceURL='https://github.com/djgraco/vocalizer-automotive-32bit-bridge',
	addon_docFileName='readme.html',
	addon_minimumNVDAVersion='2026.2',
	addon_lastTestedNVDAVersion='2026.2',
	addon_updateChannel=None,
	addon_license='GPL-2.0',
	addon_licenseURL='https://github.com/djgraco/vocalizer-automotive-32bit-bridge/blob/brokered-audio/LICENSE',

)
pythonSources = ["addon/**/*.py"]
i18nSources = pythonSources + ["buildVars.py"]
excludedFiles = ["__pycache__/*", "*.pyc", "*.pyo", "*.po", "*.pot", "*.md", "*.ps1",
                 "vocalizer_license.ini", "nuan_platform.dll?*"]
baseLanguage = "en"
markdownExtensions = ["markdown.extensions.sane_lists"]
brailleTables = {}
symbolDictionaries = {}
speechDictionaries = {}
variant = 'brokered-audio'
runtimeHashes = {'addon/synthDrivers/vocalizerAutomotive/common/speech/components/lid.dat': 'de1a14b0f6effc9db4c8792abb1af74f1c58225a9a54c938d2872c7e2ded4789', 'addon/synthDrivers/vocalizerAutomotive/common/speech/components/nuan_platform.dll': 'b23b691f7db77cbd989ffce4bf0f540b71c22cf8618469ef7618e4f5aaf7ceb8', 'addon/synthDrivers/vocalizerAutomotive/common/speech/components/synth_med_fxd_bet2f22.dat': 'f5417a45bf67f1d62fd07960337e9c64e0917c28bf0731eba9d048cf7afcc835', 'addon/synthDrivers/vocalizerAutomotive/common/speech/components/vautov5.dll': '85a02541e3a7cd6e4a7974c360d4d5433ff9e70bbd25aab6afb0cf6f80b644b4'}
restoredRuntime = {}

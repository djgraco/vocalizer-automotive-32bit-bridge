# Build metadata only. Add-on runtime source is unchanged.
from site_scons.site_tools.NVDATool.typings import AddonInfo
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
	addon_name='vocalizer_automotive_driver',
	addon_summary=_('Vocalizer Automotive 5.5 Driver'),
	addon_description=_('Driver and interface for Nuance Vocalizer Automotive 5.5.\nTo use it, you must have a valid license and install, at least, one voice downloadable from https://vocalizer-nvda.com/old/en/downloads.htm'),
	addon_version='2.1.6-2025fix',
	addon_changelog='',
	addon_author='Tiflotecnia, LDA. <tiflotecnia@tiflotecnia.com>',
	addon_url='https://github.com/djgraco/vocalizer-automotive-32bit-bridge',
	addon_sourceURL='https://github.com/djgraco/vocalizer-automotive-32bit-bridge',
	addon_docFileName='readme.html',
	addon_minimumNVDAVersion='2019.3',
	addon_lastTestedNVDAVersion='2025.1',
	addon_updateChannel=None,
	addon_license='GPL-2.0',
	addon_licenseURL='https://github.com/djgraco/vocalizer-automotive-32bit-bridge/blob/legacy-2.1.6-2025/LICENSE',

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
variant = 'legacy-2.1.6-2025'
runtimeHashes = {'addon/synthDrivers/vocalizerAutomotive/common/speech/components/lid.dat': 'de1a14b0f6effc9db4c8792abb1af74f1c58225a9a54c938d2872c7e2ded4789', 'addon/synthDrivers/vocalizerAutomotive/common/speech/components/nuan_platform.dll': 'b23b691f7db77cbd989ffce4bf0f540b71c22cf8618469ef7618e4f5aaf7ceb8', 'addon/synthDrivers/vocalizerAutomotive/common/speech/components/synth_med_fxd_bet2f22.dat': 'f5417a45bf67f1d62fd07960337e9c64e0917c28bf0731eba9d048cf7afcc835', 'addon/synthDrivers/vocalizerAutomotive/common/speech/components/vautov5.dll': '85a02541e3a7cd6e4a7974c360d4d5433ff9e70bbd25aab6afb0cf6f80b644b4'}
restoredRuntime = {'addon/synthDrivers/vocalizerAutomotive/common/speech/components/lid.dat': {'blob': '5a8d9ab7560a826897e4f9e71a4be1a18cc3cdbf', 'sha256': 'de1a14b0f6effc9db4c8792abb1af74f1c58225a9a54c938d2872c7e2ded4789'}, 'addon/synthDrivers/vocalizerAutomotive/common/speech/components/nuan_platform.dll': {'blob': '8077aba9c5e976699f3b2cc9ec8bb7db1dcfe3eb', 'sha256': 'b23b691f7db77cbd989ffce4bf0f540b71c22cf8618469ef7618e4f5aaf7ceb8'}, 'addon/synthDrivers/vocalizerAutomotive/common/speech/components/synth_med_fxd_bet2f22.dat': {'blob': '085a58a7b68e100d143bae813e9f616bef5d4c5f', 'sha256': 'f5417a45bf67f1d62fd07960337e9c64e0917c28bf0731eba9d048cf7afcc835'}, 'addon/synthDrivers/vocalizerAutomotive/common/speech/components/vautov5.dll': {'blob': '40923d890acf52e3d49e11a312d4b38788b9ebd9', 'sha256': '85a02541e3a7cd6e4a7974c360d4d5433ff9e70bbd25aab6afb0cf6f80b644b4'}}

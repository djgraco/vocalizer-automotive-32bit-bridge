import ast
import os
import types
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DRIVER_INIT_PATH = (
	REPOSITORY_ROOT
	/ "addon"
	/ "synthDrivers"
	/ "vocalizerAutomotive"
	/ "__init__.py"
)
PROXY_PATHS = [REPOSITORY_ROOT / "addon" / "synthDrivers" / "vocalizerAutomotive32.py"]
BROKERED_PROXY_PATH = (
	REPOSITORY_ROOT
	/ "variants"
	/ "brokered-audio"
	/ "addon"
	/ "synthDrivers"
	/ "vocalizerAutomotive32.py"
)
if BROKERED_PROXY_PATH.is_file():
	PROXY_PATHS.append(BROKERED_PROXY_PATH)


def _load_config_path_function(globalVars, sourcePath):
	tree = ast.parse(DRIVER_INIT_PATH.read_text(encoding="utf-8"))
	function = next(
		node
		for node in tree.body
		if isinstance(node, ast.FunctionDef)
		and node.name == "_setConfigPathFromDriverLocation"
	)
	namespace = {
		"__file__": str(sourcePath),
		"globalVars": globalVars,
		"os": os,
	}
	exec(compile(ast.Module(body=[function], type_ignores=[]), str(DRIVER_INIT_PATH), "exec"), namespace)
	return namespace[function.name]


def _proxy_driver_path(proxyPath):
	tree = ast.parse(proxyPath.read_text(encoding="utf-8"))
	driverClass = next(
		node
		for node in tree.body
		if isinstance(node, ast.ClassDef) and node.name == "SynthDriver"
	)
	assignment = next(
		node
		for node in driverClass.body
		if isinstance(node, ast.Assign)
		and any(
			isinstance(target, ast.Name) and target.id == "synthDriver32Path"
			for target in node.targets
		)
	)
	return eval(
		compile(ast.Expression(assignment.value), str(proxyPath), "eval"),
		{"__file__": str(proxyPath), "os": os},
	)


class SecureDesktopConfigPathTests(unittest.TestCase):
	def test_relative_host_config_path_is_derived_from_installed_addon(self):
		sourcePath = Path(
			r"C:\nvdaSystemConfig\addons\vocalizer_automotive_driver\synthDrivers"
			r"\vocalizerAutomotive\__init__.py"
		)
		appArgs = types.SimpleNamespace(configPath=".")
		globalVars = types.SimpleNamespace(appArgs=appArgs)
		_load_config_path_function(globalVars, sourcePath)()
		self.assertEqual(appArgs.configPath, os.path.abspath(r"C:\nvdaSystemConfig"))

	def test_absolute_config_path_from_nvda_is_preserved(self):
		configPath = os.path.abspath(r"D:\PortableNVDA")
		appArgs = types.SimpleNamespace(configPath=configPath)
		globalVars = types.SimpleNamespace(appArgs=appArgs)
		_load_config_path_function(globalVars, DRIVER_INIT_PATH)()
		self.assertEqual(appArgs.configPath, configPath)

	def test_config_path_is_set_before_dependent_driver_modules_are_imported(self):
		tree = ast.parse(DRIVER_INIT_PATH.read_text(encoding="utf-8"))
		initializerIndex = next(
			i
			for i, node in enumerate(tree.body)
			if isinstance(node, ast.Expr)
			and isinstance(node.value, ast.Call)
			and isinstance(node.value.func, ast.Name)
			and node.value.func.id == "_setConfigPathFromDriverLocation"
		)
		dependentImportIndex = next(
			i
			for i, node in enumerate(tree.body)
			if isinstance(node, ast.ImportFrom)
			and node.level == 1
			and any(alias.name in {"_languages", "_vocalizer", "_voiceManager"} for alias in node.names)
		)
		self.assertLess(initializerIndex, dependentImportIndex)

	def test_proxy_uses_its_own_synth_drivers_directory(self):
		for proxyPath in PROXY_PATHS:
			with self.subTest(proxyPath=proxyPath):
				self.assertEqual(
					os.path.normcase(_proxy_driver_path(proxyPath)),
					os.path.normcase(str(proxyPath.parent)),
				)


if __name__ == "__main__":
	unittest.main()

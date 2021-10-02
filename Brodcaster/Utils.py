import importlib
from importlib import util
import logging
import sys
from pathlib import Path


def load_plugins(plugin_name):
    path = Path(f"brodcaster/plugins/{plugin_name}.py")
    name = "plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["plugins." + plugin_name] = load
    print("importing... " + plugin_name)

import importlib
from abc import ABC, abstractstaticmethod

class PluginModule(ABC):

    @abstractstaticmethod
    def initialize():
        pass


def load_module(name: str) -> PluginModule:
    return importlib.import_module(name)


def setup_plugins(plugins: list[str]):
    for plugin in plugins:
        module = load_module(plugin)
        module.initialize()

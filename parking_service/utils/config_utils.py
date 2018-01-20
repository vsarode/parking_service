import os
from importlib import import_module
from parking_service.conf.environments import get_config_module


def get_env_config():
    agro_env = os.environ.get('AGRO_ENV', 'dev')
    module_path = get_config_module(agro_env)
    config_module = import_module(module_path)
    config = getattr(config_module, 'Config')
    return config


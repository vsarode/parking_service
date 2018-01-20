CONFIG_MAP = {
    'prod': 'production',
    'dev': 'development'
}


def get_config(env):
    return '.'.join(['parking_service', 'conf', 'environments',
                     CONFIG_MAP.get(env, env), 'Config'])


def get_config_module(env):
    return '.'.join(['parking_service', 'conf', 'environments',
                     CONFIG_MAP.get(env, env)])

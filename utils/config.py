from os import environ, path
from colorama import Fore, Style


def get_config_path():
    xdg_config = None
    if environ.get('XDG_CONFIG_HOME'):
        xdg_config = environ.get('XDG_CONFIG_HOME')
    else:
        xdg_config = path.join(path.expanduser('~'), '.config')
    return '/'.join([xdg_config, 'events_countdown.yaml'])


def create_config(config_path):
    if not path.exists(config_path):
        open(config_path, 'w')
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + Style.RESET_ALL + 'Created config at: {}'.format(config_path))

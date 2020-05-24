import sys
from os import environ, path
import yaml
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
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 'Created config at: {}'.format(config_path) + Style.RESET_ALL)


def get_events(config_path):
    events = {}
    with open(config_path, 'r') as config:
        try:
            events = yaml.safe_load(config)
        except yaml.YAMLError as e:
            print(Fore.RED + Style.BRIGHT + 'Couldn\'t load config file. {}'.format(e) + Style.RESET_ALL)
            sys.exit()
    return events

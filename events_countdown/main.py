import click

from utils.config import get_config_path, create_config
from colorama import Fore, Style


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--add', '-a', is_flag=True, help="Create events.")
@click.option('--delete', '-d', is_flag=True, help="Delete previously created events.")
@click.option('--clean', '-c', is_flag=True, help="Delete expired events.")
@click.option('--config', is_flag=True, help="Print config file path.")
def main(add, delete, clean, config):

    config_path = get_config_path()
    create_config(config_path)

    if config:
        print(Fore.BLUE + Style.BRIGHT + 'Config file path: {}'.format(config_path))

    elif add:
        print('Hello from add')


if __name__ == "__main__":
    main()

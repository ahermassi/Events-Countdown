import click

from utils.config import get_config_path, create_config, get_events
from colorama import Fore, Style
from utils.events import add_event, delete_events_interactive, delete_events, delete_expired


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--add', '-a', is_flag=True, help='Create events')
@click.option('--delete-interactive', '-di', is_flag=True, help='Delete previously created events interactively')
@click.option('--delete', '-d', multiple=True, help='Delete multiple events at once.')
@click.option('--clean', '-c', is_flag=True, help='Delete expired events')
@click.option('--config', is_flag=True, help='Print config file path')
def main(add, delete_interactive, delete, clean, config):

    config_path = get_config_path()
    create_config(config_path)
    events = [{}, get_events(config_path)][get_events(config_path) is not None]

    if add:
        add_event(config_path, events)
    elif delete:
        delete_events(config_path, events, delete)
    elif delete_interactive:
        delete_events_interactive(config_path, events)
    elif config:
        print(Fore.BLUE + Style.BRIGHT + 'Config file path: {}'.format(config_path) + Style.RESET_ALL)
    elif clean:
        delete_expired(config_path, events)
    elif not events:
        print(Fore.RED + Style.BRIGHT + 'You have no events!' + Style.RESET_ALL)


if __name__ == "__main__":
    main()

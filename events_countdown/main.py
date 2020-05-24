import click


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--add', '-a', is_flag=True, help="Add events.")
@click.option('--delete', '-d', is_flag=True, help="Delete previously added events.")
@click.option('--clean', '-c', is_flag=True, help="Delete expired events.")
@click.option('--config', is_flag=True, help="Print config file path.")
def main(add, delete=False, clean=False, config=False):

    if add:
        print('Hello from add')


if __name__ == "__main__":
    main()

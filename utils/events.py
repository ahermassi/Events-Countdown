import uuid
from datetime import date, datetime
import yaml
from colorama import Fore, Style


def get_user_input(prompt):
    answer = input(prompt).strip()
    while not answer:
        print(Fore.RED + Style.BRIGHT + 'Field can\'t be blank.' + Style.RESET_ALL)
        answer = input(prompt).strip()
    return answer


def add_event(config_path, events):
    event_name = get_user_input('Enter event name: ')
    start_date = input('Enter event start date (YYYY-MM-DD). Default is today: ').strip()
    end_date = get_user_input('Enter event end date (YYYY-MM-DD): ')
    if not start_date:
        start_date = datetime.strftime(datetime.today(), '%Y-%m-%d')

    unique_id = uuid.uuid4()
    while unique_id in events:
        unique_id = uuid.uuid4()

    events[str(uuid.uuid4())] = {'name': event_name, 'start_date': start_date, 'end_date': end_date}
    with open(config_path, 'w') as config:
        yaml.dump(events, config)
    print(Fore.GREEN + Style.BRIGHT + '{} added successfully!'.format(event_name) + Style.RESET_ALL)

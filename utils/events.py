import sys
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


def delete_events(config_path, events, events_to_delete):
    if not events:
        print(Fore.RED + Style.BRIGHT + 'You have no events!' + Style.RESET_ALL)
        sys.exit()
    if not events_to_delete:
        print(Fore.GREEN + Style.BRIGHT + 'No events to delete.')
        sys.exit()
    updated_events, events_to_delete = {}, set(events_to_delete)
    for id, event in events.items():
        if event['name'] not in events_to_delete:
            updated_events[id] = event
    bulk_delete(config_path, events_to_delete, updated_events)


def delete_events_interactive(config_path, events):
    if not events:
        print(Fore.RED + Style.BRIGHT + 'You have no events!' + Style.RESET_ALL)
        sys.exit()

    updated_events, events_to_delete = {}, []
    for id, event in events.items():
        delete = input(Fore.RED + 'Remove {} ? [y/N] '.format(event['name'])).strip().lower()
        if delete == 'y':
            events_to_delete.append(event['name'])
        else:
            updated_events[id] = event

    if not events_to_delete:
        print(Fore.GREEN + Style.BRIGHT + 'No events to delete.')
    else:
        bulk_delete(config_path, events_to_delete, updated_events)


def bulk_delete(config_path, events_to_delete, updated_events):
    print('\nThese are the events you want to delete:')
    for event in events_to_delete:
        print(Fore.BLUE + Style.BRIGHT + event + Style.RESET_ALL)
    print()
    prompt = 'Remove {} event'.format(len(events_to_delete)) + ['s?', '?'][len(events_to_delete) == 1] + ' [y/N] '
    confirm_deletion = input(Fore.RED + prompt).strip().lower()
    if confirm_deletion == 'y':
        with open(config_path, 'w') as config:
            yaml.dump(updated_events, config)
        print(Fore.GREEN + Style.BRIGHT + 'Successfully deleted.' + Style.RESET_ALL)
    else:
        print(Fore.GREEN + Style.BRIGHT + 'Aborted.' + Style.RESET_ALL)


def delete_expired(config_path, events):
    if not events:
        print(Fore.RED + Style.BRIGHT + 'You have no events!' + Style.RESET_ALL)
        sys.exit()

    updated_events, events_to_delete = {}, []
    for id, event in events.items():
        end_date = datetime.strptime(event['end_date'], "%Y-%m-%d")
        diff = (date.today() - end_date.date()).days
        if diff >= 0:
            events_to_delete.append(event['name'])
        else:
            updated_events[id] = event

    if not events_to_delete:
        print(Fore.GREEN + Style.BRIGHT + "You have no expired events.")
    else:
        bulk_delete(config_path, events_to_delete, updated_events)




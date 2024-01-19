import re


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'Enter user name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Contact not found'
    return inner


contacts = {}


@input_error
def hello_handler():
    return 'How can I help you?'


@input_error
def add_handler(command):
    pattern = r'^add [a-zA-Zа-яА-Я]{2,} \d{10,}$'
    if re.fullmatch(pattern, command):
        splitted_command = command.split()
        name = splitted_command[1]
        phone = splitted_command[2]
        if name not in contacts.keys() and phone not in contacts.values():
            contacts[name] = phone
            return (
                'Contact {name} with phone {phone} '
                'has been added to the contacts'
            ).format(name=name, phone=phone)
        else:
            raise ValueError
    else:
        return 'Invalid command. Please follow the format: add name phone'


@input_error
def change_handler(command):
    pattern = r'^change [a-zA-Zа-яА-Я]{2,} \d{10,}$'
    if re.fullmatch(pattern, command):
        splitted_command = command.split()
        name = splitted_command[1]
        phone = splitted_command[2]
        if name in contacts:
            contacts[name] = phone
            return f'Phone has been changed for {name} to {phone}'
    else:
        raise IndexError


@input_error
def phone_handler(command):
    pattern = r'^phone [a-zA-Zа-яА-Я]{2,}$'
    if re.fullmatch(pattern, command):
        splitted_command = command.split()
        name = splitted_command[1]
        if name in contacts:
            return f'The phone number for {name} is {contacts[name]}'
        else:
            raise IndexError
    else:
        raise ValueError


@input_error
def show_all_handler():
    if not contacts:
        return 'No contacts found'
    else:
        result = ''
        for key, value in contacts.items():
            result += f'{key}: {value}\n'
        return result


@input_error
def exit_handler():
    return 'Good bye!'


@input_error
def main():
    handlers_with_command = {
        'add': add_handler,
        'change': change_handler,
        'phone': phone_handler,
    }

    handlers_without_command = {
        'hello': hello_handler,
        'show all': show_all_handler,
        'good bye': exit_handler,
        'close': exit_handler,
        'exit': exit_handler
    }

    while True:
        command = input('Please enter command: ').lower()

        if command == '.' or command in ['good bye', 'close', 'exit']:
            break

        for prefix, handler in handlers_with_command.items():
            if command.startswith(prefix):
                print(handler(command))
                break
        for prefix, handler in handlers_without_command.items():
            if command.startswith(prefix):
                print(handler())
                break


if __name__ == "__main__":
    main()

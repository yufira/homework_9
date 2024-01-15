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
    splitted_command = command.split()
    name = splitted_command[1]
    phone = splitted_command[2]
    contacts[name] = phone
    return f'Contact {name} with phone {phone} has been added to the contacts'

@input_error
def change_handler(command):
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
    splitted_command = command.split()
    name = splitted_command[1]
    if name in contacts:
        return f'The phone number for {name} is {contacts[name]}'
    else:
        raise IndexError

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
    while True:
        command = input('Please enter command: ').lower()

        if command == 'hello':
            print(hello_handler())
        elif command.startswith('add'):
            print(add_handler(command))
        elif command.startswith('change'):
            print(change_handler(command))
        elif command.startswith('phone'):
            print(phone_handler(command))
        elif command == 'show all':
            print(show_all_handler())
        elif command in ['good bye', 'close', 'exit']:
            print(exit_handler())
            break
        elif command == '.':
            break


if __name__ == "__main__":
    main()

def add_contact():
    contacts.update({name: number})


def remove_contact():
    contacts.pop(name, None)


def edit_contacts():
    contacts.update({name: number})
    print("Contact successfully updated")


def save_contacts():
    f = open("contacts.txt", "w")
    f.write(str(contacts))
    f.close()
    print("Contacts successfully saved to contacts.txt")


contacts = {

}

print("Type HELP to get started... ")

while True:
    command = input("> ")
    command = command.lower()
    if command == 'help':
        print("""
ADD - To add a new contact
REMOVE - To remove a contact
EDIT - To edit a contact
SEARCH - To find a contact
VIEW - To view all existing contacts
SAVE - Outputs all contacts to a TXT file
QUIT - To exit the program
""")
    elif command == 'add':
        name = input('Name : ')
        name = name.title()
        number = input('Number : ')
        add_contact()
    elif command == 'view':
        for keys, values in contacts.items():
            print(keys)
            print(values)
    elif command == 'remove':
        name = input('Name (To be removed) : ')
        name = name.title()
        remove_contact()
    elif command == 'edit':
        print('WARNING : If name does not exist, a new entry will be added')
        name = input('Name of contact to be edited : ')
        number = input('New Number : ')
        name = name.title()
        edit_contacts()
    elif command == 'quit':
        print('Thanks for using this program!')
        break
    elif command == 'save':
        save_contacts()
    else:
        print('Invalid Command')

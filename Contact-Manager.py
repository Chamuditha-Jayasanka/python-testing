import os


CONTACTS_STORAGE_FILE = "contacts_database.txt"


def get_contacts():
    if not os.path.isfile(CONTACTS_STORAGE_FILE):
        return {}
    
    contact_list = {}
    with open(CONTACTS_STORAGE_FILE, "r") as storage:
        for entry in storage:
            name, phone_number = entry.strip().split(": ")
            contact_list[name] = phone_number
    return contact_list


def persist_contacts(contact_list):
    with open(CONTACTS_STORAGE_FILE, "w") as storage:
        for name, phone_number in contact_list.items():
            storage.write(f"{name}: {phone_number}\n")


def create_contact(contact_list):
    name = input("Enter the name of the contact: ")
    phone_number = input("Enter the phone number: ")
    contact_list[name] = phone_number
    print(f"Contact '{name}' has been successfully added.")
    persist_contacts(contact_list)


def locate_contact(contact_list):
    search_name = input("Enter the name of the contact to search: ")
    if search_name in contact_list:
        print(f"Found: {search_name} - {contact_list[search_name]}")
    else:
        print(f"No contact found for '{search_name}'.")


def display_contacts(contact_list):
    if not contact_list:
        print("The contact list is empty.")
    else:
        print("Your contacts:")
        for name, phone_number in contact_list.items():
            print(f"{name}: {phone_number}")


def remove_contact(contact_list):
    name_to_remove = input("Enter the name of the contact to remove: ")
    if name_to_remove in contact_list:
        del contact_list[name_to_remove]
        print(f"Contact '{name_to_remove}' has been removed.")
        persist_contacts(contact_list)
    else:
        print(f"Contact '{name_to_remove}' does not exist.")


def modify_contact(contact_list):
    name_to_update = input("Enter the name of the contact to update: ")
    if name_to_update in contact_list:
        new_number = input(f"Enter the new phone number for '{name_to_update}': ")
        contact_list[name_to_update] = new_number
        print(f"Contact '{name_to_update}' has been updated.")
        persist_contacts(contact_list)
    else:
        print(f"Contact '{name_to_update}' not found.")


def run_contact_book():
    contact_list = get_contacts()
    
    while True:
        print("\nContact Manager Menu:")
        print("1. Add a Contact")
        print("2. Search for a Contact")
        print("3. View All Contacts")
        print("4. Delete a Contact")
        print("5. Update a Contact")
        print("6. Exit")

        user_choice = input("Choose an option (1-6): ")

        if user_choice == '1':
            create_contact(contact_list)
        elif user_choice == '2':
            locate_contact(contact_list)
        elif user_choice == '3':
            display_contacts(contact_list)
        elif user_choice == '4':
            remove_contact(contact_list)
        elif user_choice == '5':
            modify_contact(contact_list)
        elif user_choice == '6':
            print("Closing Contact Manager. See you soon!")
            break
        else:
            print("Invalid input. Please select a valid option.")

if __name__ == "__main__":
    run_contact_book()

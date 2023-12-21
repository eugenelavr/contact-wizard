from models.AddressBook import AddressBook
from models.Contact import Contact
from services.ContactService import ContactService
from models.Note import Note
from models.NoteBook import NoteBook
from services.NoteService import NoteService
from utils.ValidationUtils import ValidationUtils
from utils.UserInput import contact_input


def main():
    contact_book = AddressBook()
    contact_service = ContactService(contact_book)
    note_book = NoteBook()
    note_service = NoteService(note_book)
    
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Search Contacts")
        print("5. Edit Contact")
        print("6. Show Contacts")
        print("7. Show Upcoming Birthdays")
        print("8. Add Note")
        print("9. Search Notes")
        print("10. Edit Note")
        print("11. Delete Note")
        print("12. Show Notes")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1": # add cont
            contact_service.add_contact(**contact_input())
            # name = input("Enter name: ").strip()
            # while not name:
            #     name = input("Name is mandatory\nEnter name: ").strip()

            # # Do validation after entering the field, if it's wrong, ask to enter again
            # phones = input("Enter phones (comma-separated): ").strip().split(",")
            # while not ValidationUtils.validate_phone(phones):
            #     phones = input("Enter phones (comma-separated, optional): ").strip().split(",")
            
            # email = input("Enter email (optional): ").strip()
            # while not ValidationUtils.validate_email(email):
            #     email = input("Enter email (optional): ").strip()
            
            # address = input("Enter address (optional): ").strip()
            
            # birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
            # while not ValidationUtils.validate_birthday(birthday):
            #     birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
            
            # contact_service.add_contact(name, address, phones, email, birthday)

        elif choice == "2": # find cont
            value = input("Enter value: ").strip()
            contacts = contact_service.find_contact(value)
            if contacts:
                print("Contact found: \n")
                for contact in contacts:
                    print(contact)
            else:
                print(f"Contact not found")

        elif choice == "3":
            name = input("Enter name: ")
            contact_service.delete_contact(name)
            print(f"Contact {name} deleted.")

        elif choice == "4":
            query = input("Enter search query: ")
            results = contact_service.search_contacts(query)
            if results:
                print("Search results:")
                for result in results:
                    print(result)
            else:
                print("No contacts found.")

        elif choice == "5":
            old_name = input("Enter the name of the contact to edit: ").strip()
            while not old_name:
                old_name = input("Name is mandatory\nEnter the name of the contact to edit: ").strip()
            
            new_name = input("Enter new name: ").strip()
            while not new_name:
                new_name = input("Name is mandatory\nEnter new name: ").strip()
            
            new_phones = input("Enter new phones (comma-separated): ").strip().split(",")
            while not ValidationUtils.validate_phone(new_phones):
                new_phones = input("Enter new phones (comma-separated): ").strip().split(",")
            
            new_email = input("Enter new email: ").strip()
            while not ValidationUtils.validate_email(new_email):
                new_email = input("Enter new email: ").strip()
            
            new_address = input("Enter new address: ").strip()
            
            new_birthday = input("Enter new birthday (DD.MM.YYYY): ").strip()
            while not ValidationUtils.validate_birthday(new_birthday):
                new_birthday = input("Enter new birthday (DD.MM.YYYY): ").strip()

            if not new_name:
                old_contact = contact_book.get(old_name.lower(), None)
                if old_contact:
                    if new_address:
                        old_contact.edit_address(new_address)
                    if new_phones:
                        for phone in new_phones:
                            old_contact.add_phone(phone)
                    if new_email:
                        old_contact.edit_email(new_email)
                    if new_birthday:
                        old_contact.edit_birthday(new_birthday)
            else:
                new_contact = Contact(new_name)
                if new_address:
                    new_contact.add_address(new_address)
                if new_phones:
                    for phone in new_phones:
                        new_contact.add_phone(phone)
                if new_email:
                    new_contact.add_email(new_email)
                if new_birthday:
                    new_contact.add_birthday(new_birthday)

            contact_service.edit_contact(old_name, new_contact)
            print(f"Contact {old_name} updated")

        elif choice == "6":
            contact_service.show_contacts()

        elif choice == "7":
            days = int(input("Enter the number of days for upcoming birthdays: "))
            upcoming_birthdays = contact_service.show_upcoming_birthdays(days)
            if upcoming_birthdays:
                print("Upcoming birthdays:")
                for contact in upcoming_birthdays:
                    print(contact)
            else:
                print("No upcoming birthdays.")

        elif choice == "8":
            note_text = input("Enter note text: ")
            note_service.add_note(note_text)
            print("Note added.")

        elif choice == "9":
            query = input("Enter search query for notes: ")
            results = note_service.search_notes(query)
            if results:
                print("Search results for notes:")
                for result in results:
                    print(result)
            else:
                print("No notes found.")

        elif choice == "10":
            old_text = input("Enter the text of the note to edit: ")
            new_text = input("Enter new note text: ")
            new_note = Note(new_text)
            note_service.edit_note(old_text, new_note)
            print(f"Note '{old_text}' updated.")

        elif choice == "11":
            note_text = input("Enter the text of the note to delete: ")
            note_service.delete_note(note_text)
            print(f"Note '{note_text}' deleted.")

        elif choice == "12":
            print(note_service.show_notes())

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

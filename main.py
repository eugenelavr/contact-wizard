from models.AddressBook import AddressBook
from models.Contact import Contact
from models.Name import Name
from models.Phone import Phone
from models.Email import Email
from models.Birthday import Birthday
from models.Address import Address
from services.contact_service import ContactService
from models.Note import Note
from models.NoteBook import NoteBook
from services.note_service import NoteService
from utils.validation_utils import ValidationUtils
from utils.user_input import contact_input


def main():
    contact_book = AddressBook()
    contact_service = ContactService(contact_book)
    note_book = NoteBook()
    note_service = NoteService(note_book)
    
    # Placeholder. Main method to be discussed.
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
            name = input("Enter name: ").strip()
            while not name:
                name = input("Name is mandatory\nEnter name: ").strip()
            contact = contact_book.get(name.lower(), None)
            if not contact:
                contact_service.add_contact(**contact_input(name = name))
            else:
                print(f"Contact with name {name} already exists")

        elif choice == "2": # find cont
            if contact_book:
                value = input("Enter value: ").strip()
                contacts = contact_service.find_contact(value)
                if contacts:
                    print("Contact found: \n")
                    for contact in contacts:
                        print(contact)
                else:
                    print(f"Contact not found")
            else:
                print("The book is empty")

        elif choice == "3":
            if contact_book:
                name = input("Enter name: ")
                contact_service.delete_contact(name)
                print(f"Contact {name} deleted.")
            else:
                print("The book is empty")

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
            if contact_book:
                old_name = input("Enter the name of the contact to edit: ").strip()
                while not old_name:
                    old_name = input("Name is mandatory\nEnter the name of the contact to edit: ").strip()
                contact = contact_book.get(old_name.lower(), None)
                if contact:
                    contact_service.edit_contact(contact, **contact_input(add=False))
                else:
                    print("Contact not found")
            else:
                print("The book is empty")

        elif choice == "6":
            if contact_book:
                contact_service.show_contacts()
            else:
                print("The book is empty")
            

        elif choice == "7":
            days = int(input("Enter the number of days for upcoming birthdays: "))
            contact_service.show_upcoming_birthdays(days)

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

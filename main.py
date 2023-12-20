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

        if choice == "1":
            name = input("Enter name: ")
            address = input("Enter address (optional): ")
            phones = input("Enter phones (comma-separated): ").split(",")
            emails = input("Enter emails (comma-separated): ").split(",")
            birthday = input("Enter birthday (DD.MM.YYYY): ")

            contact_service.add_contact(name, address, phones, emails, birthday)

        elif choice == "2":
            name = input("Enter name: ")
            contact = contact_service.find_contact(name)
            if contact:
                print(f"Contact found: {contact}")
            else:
                print(f"Contact not found with name: {name}")

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
            old_name = input("Enter the name of the contact to edit: ")
            new_name = input("Enter new name: ")
            new_address = input("Enter new address (optional): ")
            new_phones = input("Enter new phones (comma-separated): ").split(",")
            new_emails = input("Enter new emails (comma-separated): ").split(",")
            new_birthday = input("Enter new birthday (DD.MM.YYYY): ")

            new_contact = Contact(new_name)
            if new_address:
                new_contact.address = Address(new_address)
            if new_phones:
                for phone in new_phones:
                    new_contact.add_phone(phone)
            if new_emails:
                for email in new_emails:
                    new_contact.add_email(email)
            if new_birthday:
                new_contact.add_birthday(new_birthday)

            contact_service.edit_contact(old_name, new_contact)
            print(f"Contact {old_name} updated.")

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

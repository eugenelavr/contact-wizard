from models.Contact import Contact, AddressBook
from services.ContactService import ContactService
from models.Note import Note, NoteBook
from services.NoteService import NoteService
from utils.ValidationUtils import ValidationUtils

def show_menu():
    print(
    """
     \nOptions:
     1. Add Contact
     2. Find Contact
     3. Edit Contact
     4. Delete Contact
     5. Show Contacts
     6. Show Upcoming Birthdays
     7. Add Note
     8. Search Notes
     9. Edit Note
     10. Delete Note
     11. Show Notes
     0. Exit
    """
    )
    
def main():
    
    #contacts = load_contacts()
    show_menu()
    
    contact_book = AddressBook()
    contact_service = ContactService(contact_book)
    note_book = NoteBook()
    note_service = NoteService(note_book)
    
    while True:
        choice = input("Enter your choice № of command or + to show all commands: ")

        if choice == "1" or choice.lower().startswith("add contact"): 
            name = input("Enter name: ").strip()
            while not name:
                name = input("Name is mandatory\nEnter name: ").strip()

            phones = input("Enter phones (comma-separated): ").strip().split(",")
            while not ValidationUtils.validate_phone_list(phones):
                phones = input("Enter phones (comma-separated, optional): ").strip().split(",")
            
            email = input("Enter email (comma-separated, optional): ").strip()
            while not ValidationUtils.validate_email(email):
                email = input("Enter email (comma-separated, optional): ").strip()
            
            address = input("Enter address (optional): ").strip()
            
            birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
            while not ValidationUtils.validate_birthday(birthday):
                birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
            
            contact_service.add_contact(name, address, phones, email, birthday)

        elif choice == "2" or choice.lower().startswith("find contact"): 
            value = input("Enter value: ").strip()
            contacts = contact_service.find_contact(value)
            if contacts:
                print("Contact found: \n")
                for contact in contacts:
                    print(contact)
            else:
                print(f"Contact not found.")

        elif choice == "3" or choice.lower().startswith("edit contact"):
            old_name = input("Enter the name of the contact to edit: ").strip()
            while not old_name:
                old_name = input("Name is mandatory\nEnter the name of the contact to edit: ").strip()
            
            new_name = input("Enter new name: ").strip()
            while not new_name:
                new_name = input("Name is mandatory\nEnter new name: ").strip()
            
            new_phones = input("Enter new phones (comma-separated): ").strip().split(",")
            while not ValidationUtils.validate_phone_list(new_phones):
                new_phones = input("Enter new phones (comma-separated): ").strip().split(",")
            
            new_email = input("Enter new email: ").strip()
            while not ValidationUtils.validate_email(new_email):
                new_email = input("Enter new email (comma-separated): ").strip()
            
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
            
        elif choice == "4" or choice.lower().startswith("delete contact"):
            name = input("Enter contact name to delete: ")
            contact_service.delete_contact(name)
            print(f"Contact {name} deleted.")

        elif choice == "5" or choice.lower().startswith("show contacts"):
            print(contact_service.show_contacts())

        elif choice == "6" or choice.lower().startswith("show upcoming birthdays"):
            days = int(input("Enter the number of days for upcoming birthdays: "))
            upcoming_birthdays = contact_service.show_upcoming_birthdays(days)
            if upcoming_birthdays:
                print("Upcoming birthdays:")
                for contact in upcoming_birthdays:
                    print(contact)
            else:
                print("No upcoming birthdays.")

        elif choice == "7" or choice.lower().startswith("add note"):
            note_name = input("Enter note name: ")
            note_text = input("Enter note text: ")
            note_service.add_note(note_name, note_text)
            print("Note added.")

        elif choice == "8" or choice.lower().startswith("search notes"):
            query = input("Enter search query for notes: ")
            results = note_service.search_notes(query)
            if results:
                print("Search results for notes:")
                for result in results:
                    print(result)
            else:
                print("No notes found.")

        elif choice == "9" or choice.lower().startswith("edit note"):
            note_name = input("Enter the name of the note to edit: ")
            new_text = input("Enter new note text: ")
            new_note = Note(note_name, new_text)
            note_service.edit_note(note_name, new_note)
            print(f"Note '{note_name}' updated.")

        elif choice == "10" or choice.lower().startswith("delete note"):
            note_name = input("Enter the name of the note to delete: ")
            note_service.delete_note(note_name)
            print(f"Note '{note_name}' deleted.")

        elif choice == "11" or choice.lower().startswith("show notes"):
            print(note_service.show_notes())

        elif choice == "0" or choice.lower().startswith("exit"):
            print("Goodbye!")
            break

        elif choice == "+":
            show_menu()

        else:
            print("Invalid choice. Please try again.")
            show_menu()

if __name__ == "__main__":
    main()

from models.contact import Contact, AddressBook
from services.ContactService import ContactService
from models.note import Note, NoteBook
from services.NoteService import NoteService
from utils.ValidationUtils import ValidationUtils
from utils.user_input import contact_input

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
        choice = input("\nEnter your choice № or command: ")

        if choice == "1" or choice.lower().startswith("add contact"): 
            name = input("Enter name: ").strip()
            while not name:
                name = input("Name is mandatory\nEnter name: ").strip()
            contact = contact_book.get(name.lower(), None)
            if not contact:
                contact_service.add_contact(**contact_input(name = name))
            else:
                print(f"Contact with name {name} already exists")

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
            
        elif choice == "4" or choice.lower().startswith("delete contact"):
            name = input("Enter contact name to delete: ")
            contact_service.delete_contact(name)
            print(f"Contact {name} deleted.")

        elif choice == "5" or choice.lower().startswith("show contacts"):
            print(contact_service.show_contacts())

        elif choice == "6" or choice.lower().startswith("show upcoming birthdays"):
            days = int(input("Enter the number of days for upcoming birthdays: "))
            contact_service.show_upcoming_birthdays(days)

        elif choice == "7" or choice.lower().startswith("add note"):
            note_text = input("Enter note text: ")
            note_service.add_note(note_text)
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
            old_text = input("Enter the text of the note to edit: ")
            new_text = input("Enter new note text: ")
            new_note = Note(new_text)
            note_service.edit_note(old_text, new_note)
            print(f"Note '{old_text}' updated.")

        elif choice == "10" or choice.lower().startswith("delete note"):
            note_text = input("Enter the text of the note to delete: ")
            note_service.delete_note(note_text)
            print(f"Note '{note_text}' deleted.")

        elif choice == "11" or choice.lower().startswith("show notes"):
            print(note_service.show_notes())

        elif choice == "0" or choice.lower().startswith("exit"):
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            show_menu()

if __name__ == "__main__":
    main()

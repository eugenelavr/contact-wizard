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
from utils.ValidationUtils import ValidationUtils
from utils.user_input import contact_input, note_input

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
    contact_book = AddressBook()
    contact_service = ContactService(contact_book)
    note_book = NoteBook()
    note_service = NoteService(note_book)
    
    show_menu()
    
    while True:
        
        choice = input("\nEnter command: ")
        
        if "add" in choice.lower() or choice in ["1", "7"]:

            if "contact" in choice or choice == "1":
                name = input("Enter name: ").strip()
                while not name:
                    name = input("Name is mandatory\nEnter name: ").strip()
                contact = contact_book.get(name.lower(), None)
                if not contact:
                    contact_service.add_contact(**contact_input(name = name))
                else:
                    print(f"Contact with name {name} already exists")
            
            if "note" in choice.lower() or choice == "7":
                if note_service.add_note(**note_input()):
                    print("Note added")
        
        elif any(word in choice.lower() for word in ["edit", "change"]) or choice in ["3", "9"]:

            if "contact" in choice or choice == "3":
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
            
            if "note" in choice.lower() or choice == "9":
                if note_book:
                    note_service.show_notes()
                    id = input("Enter ID of the note: ").strip()
                    while not id.isdigit():
                        id = input("ID must be a number\nEnter ID of the note: ").strip()
                    note_service.edit_note(id, Note(**note_input(add=False)))
                else:
                    print("There is no notes")
        
        elif "delete" in choice.lower() or choice in ["4", "10"]:

            if "contact" in choice or choice == "4":
                if contact_book:
                    name = input("Enter name: ")
                    contact_service.delete_contact(name)
                    print(f"Contact {name} deleted.")
                else:
                    print("The book is empty")
            
            if "note" in choice.lower() or choice == "10":
                if note_book:
                    note_service.show_notes()
                    id = input("Enter ID of the note: ").strip()
                    while not id.isdigit():
                        id = input("ID must be a number\nEnter ID of the note: ").strip()
                    note_service.delete_note(id)
                else:
                    print("There is no notes")

        elif any(word in choice.lower() for word in ["find", "search"]) or choice in ["2", "8"]:
            
            if "contact" in choice or choice == "2":
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
            
            if "note" in choice.lower() or choice == "8":
                if note_book:
                    query = input("Enter search query for notes: ")
                    results = note_service.search_notes(query)
                    if results:
                        print("Search results for notes:")
                        for result in results:
                            print(result)
                    else:
                        print("No notes found.")
                else:
                    print("There is no notes")

        elif any(word in choice.lower() for word in ["all", "show"])  or choice in ["5", "6", "11"]:
            
            if "contact" in choice or choice == "5":
                if contact_book:
                    contact_service.show_contacts()
                else:
                    print("The book is empty")

            if "birthday" in choice  or choice == "6":
                if contact_book:
                    days = int(input("Enter the number of days for upcoming birthdays: "))
                    contact_service.show_upcoming_birthdays(days)
                else:
                    print("The book is empty")
            
            if "note" in choice.lower() or choice == "11":
                if note_book:
                    note_service.show_notes()
                else:
                    print("There is no notes")
        
        elif any(word in choice.lower() for word in ["exit", "close", "end", "bye"])  or choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again")

        # if choice == "1": # add cont
        #     name = input("Enter name: ").strip()
        #     while not name:
        #         name = input("Name is mandatory\nEnter name: ").strip()
        #     contact = contact_book.get(name.lower(), None)
        #     if not contact:
        #         contact_service.add_contact(**contact_input(name = name))
        #     else:
        #         print(f"Contact with name {name} already exists")

        # elif choice == "2": # find cont
        #     if contact_book:
        #         value = input("Enter value: ").strip()
        #         contacts = contact_service.find_contact(value)
        #         if contacts:
        #             print("Contact found: \n")
        #             for contact in contacts:
        #                 print(contact)
        #         else:
        #             print(f"Contact not found")
        #     else:
        #         print("The book is empty")

        # elif choice == "3": # edit cont
        #     if contact_book:
        #         old_name = input("Enter the name of the contact to edit: ").strip()
        #         while not old_name:
        #             old_name = input("Name is mandatory\nEnter the name of the contact to edit: ").strip()
        #         contact = contact_book.get(old_name.lower(), None)
        #         if contact:
        #             contact_service.edit_contact(contact, **contact_input(add=False))
        #         else:
        #             print("Contact not found")
        #     else:
        #         print("The book is empty")

        # elif choice == "4": # delete cont
        #     if contact_book:
        #         name = input("Enter name: ")
        #         contact_service.delete_contact(name)
        #         print(f"Contact {name} deleted.")
        #     else:
        #         print("The book is empty")
        

        # elif choice == "5":
        #     if contact_book:
        #         contact_service.show_contacts()
        #     else:
        #         print("The book is empty")
            

        # elif choice == "6":
        #     days = int(input("Enter the number of days for upcoming birthdays: "))
        #     contact_service.show_upcoming_birthdays(days)

        # elif choice == "7":
        #     note_text = input("Enter note text: ")
        #     note_service.add_note(note_text)
        #     print("Note added.")

        # elif choice == "8":
        #     query = input("Enter search query for notes: ")
        #     results = note_service.search_notes(query)
        #     if results:
        #         print("Search results for notes:")
        #         for result in results:
        #             print(result)
        #     else:
        #         print("No notes found.")

        # elif choice == "9":
        #     old_text = input("Enter the text of the note to edit: ")
        #     new_text = input("Enter new note text: ")
        #     new_note = Note(new_text)
        #     note_service.edit_note(old_text, new_note)
        #     print(f"Note '{old_text}' updated.")

        # elif choice == "10":
        #     note_text = input("Enter the text of the note to delete: ")
        #     note_service.delete_note(note_text)
        #     print(f"Note '{note_text}' deleted.")

        # elif choice == "11":
        #     print(note_service.show_notes())

        # elif choice == "0":
        #     print("Goodbye!")
        #     break

        # else:
        #     print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import json
import re
from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta
import os

contacts_file = "contacts.json"

def load_contacts():
    if os.path.exists(contacts_file):
        with open(contacts_file) as f:
            return json.load(f)
    else:
        return {}
        
def save_contacts(contacts):
    with open(contacts_file, 'w') as f: 
        json.dump(contacts, f, indent=4)

@dataclass
class Contact:
    name: str
    phone: str 
    email: str
    birthday: date
    
def is_valid_phone(phone):
    if re.match(r'\d{12,}$', phone):
        return True
    return False

def is_valid_email(email):
    # Email validation
    pass #Email validation in console bot considered as bullshit
    
def add_contact(contacts):
    print("Enter details to add contact")
    name = input("Name: ")
    phone = input("Phone number (at least 12 digits): ")
    if not is_valid_phone(phone):
        print("Invalid phone number")
        return 
    
    email = input("Email address: ")
    if not is_valid_email(email):
        print("Invalid email")
        return  
        
    birthday = input("Birthday (YYYY-MM-DD): ")  
    contacts[name] = asdict(Contact(name, phone, email,  
            birthday=datetime.strptime(birthday,"%Y-%m-%d").date()))
    print(f"'{name}' contact added successfully!")
    save_contacts(contacts)
    
def search_contacts(contacts):
    search = input("Enter search name/phone/email: ")
    results = []
    for name, details in contacts.items():
        if search in name or search in details['phone'] or search in details['email']:
            results.append(name)
            
    if results:
        print("Search results:")
        for name in results:  
            print(f"- {name}")
    else:
        print("No contacts found for the search")
        
def edit_contact(contacts):
    name = input("Enter contact name to edit: ") 
    if name not in contacts:
        print("Contact not found!")
        return
        
    print("Enter updated details (blank for no change) -")
    phone = input("Updated phone number: ")   
    if phone and not is_valid_phone(phone):
        print("Invalid phone number") 
        return   
        
    email = input("Updated email: ")
    if email and not is_valid_email(email):
        print("Invalid email")
        return
        
    birthday = input("Updated birthday - YYYY-MM-DD: ")
    if birthday:
        birthday = datetime.strptime(birthday, "%Y-%m-%d").date() 
    else:
        birthday = contacts[name]['birthday']
        
    contacts[name] = asdict(Contact(name, phone or contacts[name]['phone'], email or contacts[name]['email'], birthday)) 
    print(f"{name} contact updated successfully!")
    save_contacts(contacts)
    
def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name not in contacts:
        print("Contact not found!")
        return

    confirmation = input(f"Are you sure you want to delete {name} (Y/N)?").lower()  
    if confirmation == "y":
        del contacts[name]
        print(f"{name} contact deleted successfully!") 
        save_contacts(contacts)
    else:
        print("Deletion cancelled!")

def upcoming_birthdays(contacts):  
    upcoming_days = 7
    today = datetime.today().date()
    
    print(f"Birthdays in upcoming {upcoming_days} days:")
    for name, details in contacts.items():
        birthday = details['birthday']
        days_to_birthday = (birthday - today).days  
        if 0 <= days_to_birthday <= upcoming_days:
            print(name + "'s birthday is on", birthday)
            
    save_contacts(contacts)
            
def show_menu():
    print(
    """
    1. Add new contact
    2. Search contacts  
    3. Edit contact
    4. Delete contact
    5. Upcoming birthdays 
    6. Show menu
    7. Exit
    """
    )
    
def main():
    contacts = load_contacts()
    show_menu()
    
    while True:  
        option = input("Enter option: ")
        if option == "1":
            add_contact(contacts)
        elif option == "2":
            search_contacts(contacts)
        elif option == "3":
            edit_contact(contacts)
        elif option == "4":
            delete_contact(contacts)
        elif option == "5":
            upcoming_birthdays(contacts)
        elif option == "6":
            show_menu()
        elif option == "7":
            print("Goodbye!")
            break  
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
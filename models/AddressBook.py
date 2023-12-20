from collections import UserDict
from datetime import datetime
from models.Contact import Contact

class AddressBook(UserDict):
    
    def add_contact(self, contact:Contact):
        if self.data and (contact.name.value.lower() in self.data):
            print(f"Contact with name {contact.name.value} already exists")
        else:
            self.data[contact.name.value.lower()] = contact
            print("Contact added")
    
    # OLD
    # def add_contact(self, contact):
    #     if contact.name.value in self.data:
    #         raise ValueError(f"Contact with name {contact.name.value} already exists in the address book")
    #     self.data[contact.name.value] = contact

    def find_contact(self, name):
        return self.data.get(name)

    def delete_contact(self, name):
        # Placeholder delete_contact. Rewrite test code below
        if name in self.data:
            del self.data[name]

    # def search_contacts(self, query):
    #     # Placeholder search_contacts. Rewrite test code below
    #     return [contact for contact in self.data.values() if query.lower() in contact.name.value.lower()]

    def edit_contact(self, old_name, new_contact):
        # Placeholder edit_contact. Rewrite test code below
        if old_name in self.data:
            del self.data[old_name]
            self.add_contact(new_contact)
        else:
            raise ValueError(f"Contact with name {old_name} not found in the address book")

    def show_contacts(self):
        if self.data:
            result = "All contacts:\n"
            for contact in self.data.values():
                print(contact)
            #     result += f"{contact}\n"
            # return result.strip()
        else:
            print("No contacts found.")

    def show_upcoming_birthdays(self, days):
        # Placeholder > Showing birthday date. Rewrite test code below (test copied from hw)
        today = datetime.today()
        upcoming_birthdays = []

        for contact in self.data.values():
            if contact.birthday:
                birthday_date = datetime.strptime(contact.birthday.value, '%d.%m.%Y')
                days_until_birthday = (birthday_date - today).days
                if 0 <= days_until_birthday <= days:
                    upcoming_birthdays.append(contact)

        return upcoming_birthdays
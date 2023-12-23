from collections import UserDict
from datetime import datetime
from models.Contact import Contact
from utils.validation_utils import ValidationUtils

class AddressBook(UserDict):
    
    def add_contact(self, contact:Contact):
        self.data[contact.name.value.lower()] = contact
        return True # if adding is successful

    def find_contact(self, value):
        contacts = set()
        if ValidationUtils.validate_phone(value):
            for contact in self.data.values():
                for phone in contact.phones:
                    if phone.value == value:
                        contacts.add(contact)
        elif ValidationUtils.validate_email(value):
            for contact in self.data.values():
                if contact.email.value == value:
                    contacts.add(contact)
        elif ValidationUtils.validate_birthday(value):
            for contact in self.data.values():
                if contact.birthday.value == datetime.strptime(value, "%d.%m.%Y").date():
                    contacts.add(contact)
        else:
            for contact in self.data.values():
                if contact.address.value == value:
                    contacts.add(contact)
            contact_by_name = self.data.get(value, None)
            if contact:
                contacts.add(contact_by_name)
        return contacts

    def delete_contact(self, name):
        # Placeholder delete_contact. Rewrite test code below
        if name in self.data:
            del self.data[name]
        else:
            print("Contact not found")

    def search_contacts(self, query):
        # Placeholder search_contacts. Rewrite test code below
        return [contact for contact in self.data.values() if query.lower() in contact.name.value.lower()]

    def edit_contact(self, old_name, new_contact):
        # Placeholder edit_contact. Rewrite test code below
        if old_name.lower() in self.data:
            del self.data[old_name.lower()]
            self.add_contact(new_contact)
        else:
            print(f"Contact {old_name} was not found")

    def show_contacts(self):
        sorted_dict = dict(sorted(self.data.items()))
        for contact in sorted_dict.values():
            print(contact)

    def show_upcoming_birthdays(self, days):
        # Placeholder > Showing birthday date. Rewrite test code below (test copied from hw)
        # today = datetime.today()
        # upcoming_birthdays = []

        # for contact in self.data.values():
        #     if contact.birthday:
        #         birthday_date = datetime.strptime(contact.birthday.value, '%d.%m.%Y')
        #         days_until_birthday = (birthday_date - today).days
        #         if 0 <= days_until_birthday <= days:
        #             upcoming_birthdays.append(contact)
        
        # return upcoming_birthdays

        upcoming_birthday_list = []
    
        current_date = datetime.now().date()
        
        for contact in self.data.values():
            # Calculate the upcoming birthday date for the current year
            upcoming_birthday = contact.birthday.value.replace(year=current_date.year)

            # If the upcoming birthday is within the specified number of days
            if (upcoming_birthday - current_date).days < 0:
                upcoming_birthday = contact.birthday.value.replace(year = current_date.year + 1)
            if (upcoming_birthday - current_date).days <= days:
                upcoming_birthday_list.append(contact)
        
        if upcoming_birthday_list:
            print(f"Upcoming birthdays in the next {days} days:")
            for contact in upcoming_birthday_list:
                print(
                    f"{contact.name.value}'s birthday is on {datetime.strftime(contact.birthday.value, "%d %B")}" #  - Phone: {contact.phone} - Email: {contact.email}
                )
        else:
            print("No upcoming birthdays in the specified days.")

        
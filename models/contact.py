from datetime import datetime
from models.field import Field
from collections import UserDict

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        # Placeholder for phone validation call
        super().__init__(value)

class Email(Field):
    def __init__(self, value):
        # Placeholder for email validation call
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid birthday format. Please use DD.MM.YYYY.")
        super().__init__(value)

class Address(Field):
    pass

class Contact:
    def __init__(self, name):
        self.name = Name(name)
        self.address = None
        self.phones = []
        self.emails = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def add_email(self, email):
        self.emails.append(Email(email))

    def remove_email(self, email):
        if email in self.emails:
            self.emails.remove(email)

    def add_birthday(self, birthday):
        if self.birthday is not None:
            raise ValueError("Birthday already exists for this contact")
        self.birthday = Birthday(birthday)

    def __str__(self):
        result = f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}, emails: {'; '.join(str(e) for e in self.emails)}"
        if self.address:
            result += f", address: {self.address.value}"
        if self.birthday:
            result += f", birthday: {self.birthday}"
        return result

class AddressBook(UserDict):
    def add_contact(self, contact):
        if contact.name.value in self.data:
            raise ValueError(f"Contact with name {contact.name.value} already exists in the address book")
        self.data[contact.name.value] = contact

    def find_contact(self, name):
        return self.data.get(name)

    def delete_contact(self, name):
        # Placeholder delete_contact. Rewrite test code below
        if name in self.data:
            del self.data[name]

    def search_contacts(self, query):
        # Placeholder search_contacts. Rewrite test code below
        return [contact for contact in self.data.values() if query.lower() in contact.name.value.lower()]

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
                result += f"{contact}\n"
            return result.strip()
        else:
            return "No contacts found."

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
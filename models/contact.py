from datetime import datetime, timedelta
from models.Field import Field
from collections import UserDict

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        
class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        
class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            print("Invalid birthday format. Please use DD.MM.YYYY.")
        super().__init__(value)

class Address(Field):
    pass
    
class Contact:
    def __init__(self, name):
        self.name = Name(name)
        self.address = None
        self.phone = None
        self.email = None
        self.birthday = None
    
    def add_phone(self, phone):
        self.phone = Phone(phone)

    def edit_phone(self, old_phone_number, new_phone_number):
        self.phone = Phone(new_phone_number)

    def remove_phone(self):
        self.phone = None
    
    def add_email(self, email):
        self.email = Email(email)
    
    def edit_email(self, email):
        self.email = Email(email)

    def remove_email(self):
        self.email = None

    def add_address(self, address):
        self.address = Address(address)
    
    def edit_address(self, address):
        self.address = Address(address)

    def remove_address(self):
        self.address = None
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def edit_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def remove_birthday(self):
        self.birthday = None

    def __str__(self):
        result = f"name: {self.name.value}, phone: {self.phone.value}, email: {self.email.value}, address: {self.address.value}, birthday: {self.birthday}"
        return result
    
class AddressBook(UserDict):
    def add_contact(self, contact):
        if contact.name.value in self.data:
            print(f"Contact with name {contact.name.value} already exists in the address book")
            return

        self.data[contact.name.value] = contact
        print(f"Contact added: {contact.name.value}\n")
    
    def find_contact(self, keyword):
        results = []

        for record in self.data.values():
            match = False

            if record.name.value.lower() == keyword.lower():
                match = True
            if record.phone and record.phone.value.lower() == keyword.lower():
                match = True
            if record.address and record.address.value.lower() == keyword.lower():
                match = True
            if record.email and record.email.value.lower() == keyword.lower():
                match = True
            if record.birthday and record.birthday.value.lower() == keyword.lower():
                match = True
            if match:
                results.append(record)

        return results

    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]

    def edit_contact(self, old_name, new_contact):
        if old_name in self.data:
            del self.data[old_name]
            self.add_contact(new_contact)
            print(f"Contact {old_name} updated")
        else:
            print (f"Contact with name {old_name} not found in the address book, abort update operation.")

    def show_contacts(self):
        if self.data:
            result = "All contacts:\n"
            for contact in self.data.values():
                result += f"{contact}\n"
            return result.strip()
        else:
            return "No contacts found."
        
    def setialized(self):
        data = {}
        for key, value in self.data.items():
            data[key] = value.__str__()
        return data

    def show_upcoming_birthdays(self, upcoming_days=7):
        today = datetime.today()
        next_period_end = today + timedelta(days=upcoming_days)

        upcoming_birthdays = []

        for record_name, record in self.data.items():
            if record.birthday:
                if isinstance(record.birthday, Birthday):
                    birthday_date = datetime.strptime(record.birthday.value, '%d.%m.%Y')
                elif isinstance(record.birthday, str):
                    birthday_date = datetime.strptime(record.birthday, '%d.%m.%Y')
                else:
                    print ("Unsupported birthday format")

                # Ignore the year in the comparison
                birthday_date = birthday_date.replace(year=today.year)

                print(f"Comparing birthday for {record_name}: {birthday_date}, Today: {today}, Next period end: {next_period_end}")

                if today <= birthday_date <= next_period_end:
                    upcoming_birthdays.append(record_name)

        return upcoming_birthdays
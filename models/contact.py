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
        self.phones = []
        self.emails = []
        self.birthday = None
    
    def add_phone(self, phone):
        if phone not in self.phones:
             self.phones.append(Phone(phone))
        else: print("Number already exists")

    def edit_phone(self, old_phone_number, new_phone_number):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone_number:
                self.phones[index] = Phone(new_phone_number)
                break
            else:
                print("Old phone number not found")

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
    
    def add_email(self, email):
        if email not in self.emails:
            self.emails.append(Email(email))
        else:
            print("Email already exists")
    
    def edit_email(self, email):
        self.email = Email(email)

    def remove_email(self, email):
        if email in self.emails:
            self.emails.remove(email)
    
    def add_address(self, address):
        if address is not None:
            self.address = Address(address)
    
    def edit_address(self, address):
        self.address = Address(address)

    def remove_address(self, address):
        self.address = None
    
    def add_birthday(self, birthday):
        if self.birthday is not None:
            raise ValueError("Birthday already exists for this contact")
        self.birthday = Birthday(birthday)

    def edit_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def remove_birthday(self, birthday):
        self.birthday = None

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
            if record.phones and any(phone.value.lower() == keyword.lower() for phone in record.phones):
                match = True
            if record.address and keyword.lower() in record.address.value.lower():
                match = True
            if record.emails and any(email.value.lower() == keyword.lower() for email in record.emails):
                match = True
            if record.birthday and keyword.lower() in record.birthday.value.lower():
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
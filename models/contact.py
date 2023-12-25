from datetime import datetime, timedelta
from models.field import Field
from collections import UserDict

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        
class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        
class Birthday(Field):
    def __init__(self, value):
        self.__value = value
        super().__init__(value)
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = datetime.strptime(value, "%d.%m.%Y").date()

class Address(Field):
    def __init__(self, value):
        super().__init__(value)
    
class Contact:
    def __init__(self, name):
        self.__name = Name(name)
        self.address = None
        self.phones = []
        self.email = None
        self.birthday = None
    
    @property
    def name(self):
        return self.__name
    
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
        if self.email:
            print("Email already exists")
        else:
            if email:
                self.email = Email(email)
    
    def edit_email(self, email):
        self.email = Email(email)

    def remove_email(self):
        self.email = None
    
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
        result = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        if self.email:
            result += f", email: {self.email.value}"
        if self.address:
            result += f", address: {self.address.value}"
        if self.birthday:
            result += f", birthday: {datetime.strftime(self.birthday.value, "%d.%m.%Y")}"
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
            if record.email and any(email.value.lower() == keyword.lower() for email in record.email):
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
            result = "\nAll contacts:\n"
            for contact in self.data.values():
                result += f"{contact}\n"
            return result.strip()
        else:
            return "No contacts found."

    def show_upcoming_birthdays(self, days):
        upcoming_birthday_list = []
    
        current_date = datetime.now().date()
        
        for contact in self.data.values():
            # Calculate the upcoming birthday date for the current year
            if not contact.birthday:
                continue
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
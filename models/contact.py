from datetime import datetime
from models.Name import Name
from models.Phone import Phone
from models.Email import Email
from models.Birthday import Birthday
from models.Address import Address


class Contact:
    def __init__(self, name):
        self.name = Name(name)
        self.address = None
        self.phones = []
        self.email = None
        self.birthday = None
    
    # Phone actions
    def add_phone(self, phone):
        for phone_ in self.phones:
            if phone_.value == phone:
                print("Number already exists")
                return
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones.remove(phone)
                self.phones.insert(index, Phone(new_phone))

    def remove_phone(self, phone):
        for phone_ in self.phones:
            if phone_.value == phone:
                self.phones.remove(phone_)
    
    # Email actions
    def add_email(self, email):
        if self.email:
            print("Email already exists")
        else:
            self.email = Email(email)
    
    def edit_email(self, email):
        self.email = Email(email)

    def remove_email(self, email):
        self.email = None
    
    # Address actions
    def add_address(self, address):
        if self.address:
            print("Address already exists")
        else:
            self.address = Address(address)
    
    def edit_address(self, address):
        self.address = Address(address)

    def remove_address(self, address):
        self.address = None
    
    #Birthday actions
    def add_birthday(self, birthday):
        if self.birthday:
            print("Birthday already exists")
            # raise ValueError("Birthday already exists for this contact")
        else:
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

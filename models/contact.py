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
        pass

    def remove_phone(self, phone):
        pass
        # if phone in self.phones:
        #     self.phones.remove(phone)
    
    # Email actions
    def add_email(self, email):
        if self.email:
            print("Email already exists")
        else:
            self.email = Email(email)
        # self.emails.append(Email(email))
    
    def edit_email(self, email):
        pass

    def remove_email(self, email):
        self.email = None
        # if email in self.emails:
        #     self.emails.remove(email)
    
    # Address actions
    def add_address(self, address):
        if self.address:
            print("Address already exists")
        else:
            self.address = Address(address)
    
    def edit_address(self, address):
        pass

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
        pass

    def remove_birthday(self, birthday):
        pass

    def __str__(self):
        result = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, email: {self.email.value}"
        if self.address:
            result += f", address: {self.address.value}"
        if self.birthday:
            result += f", birthday: {self.birthday.value}"
        return result

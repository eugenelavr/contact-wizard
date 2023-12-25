from models.Contact import Contact, AddressBook
import json

class ContactService:
    def __init__(self, address_book : AddressBook):
        self.address_book = address_book

    def fill_from_file(self, contacts):
        for key, value in contacts.items():
            dictionary = {}

            for item in value.split(", "):
                i, value = item.split(": ")
                dictionary[i] = value

            address = dictionary['address'] if dictionary['address'] else None
            phone = dictionary['phone'] if dictionary['phone'] else None
            email = dictionary['email'] if dictionary['email']  else None
            birthday = dictionary['birthday'] if dictionary['birthday'] else None

            self.add_contact(key, address, phone, email, birthday)

    def add_contact(self, name, address=None, phone=None, email=None, birthday=None):
        contact = Contact(name)

        if address:
            contact.add_address(address)
        if phone:
            contact.add_phone(phone.strip())
        if email:
            contact.add_email(email)
        if birthday:
            contact.add_birthday(birthday)

        self.address_book.add_contact(contact)

    def find_contact(self, value):
        return self.address_book.find_contact(value)

    def delete_contact(self, name):
        self.address_book.delete_contact(name)

    def edit_contact(self, old_name, new_contact):
        self.address_book.edit_contact(old_name, new_contact)

    def show_contacts(self):
        return self.address_book.show_contacts()

    def show_upcoming_birthdays(self, days):
        return self.address_book.show_upcoming_birthdays(days)
    
    def get_all_contacts(self):
        return self.address_book.setialized()

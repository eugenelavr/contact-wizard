import re
from models.Contact import Contact
from models.AddressBook import AddressBook

class ContactService:
    def __init__(self, address_book : AddressBook):
        self.address_book = address_book

    def add_contact(self, name, address=None, phones=None, email=None, birthday=None):
        contact = Contact(name)
        if address:
            contact.add_address(address)
        if phones:
            for phone in phones:
                contact.add_phone(phone.strip())
        if email:
            contact.add_email(email)
        if birthday:
            contact.add_birthday(birthday)

        if self.address_book.add_contact(contact):
            print("Contact added")

    def find_contact(self, value):
        return self.address_book.find_contact(value)

    def delete_contact(self, name):
        self.address_book.delete_contact(name)

    # def search_contacts(self, query):
    #     return self.address_book.search_contacts(query)

    def edit_contact(self, contact, name, address=None, phones=None, email=None, birthday=None):
        new_contact = None
        if name:
            new_contact = Contact(name)
            if contact.email:
                new_contact.add_email(contact.email.value)
            if contact.address:
                new_contact.add_address(contact.address.value)
            if contact.birthday:
                new_contact.add_birthday(contact.birthday.value)
            if contact.phones:
                for phone in contact.phones:
                        new_contact.add_phone(phone.value)
        else:
            new_contact = contact
        
        if phones and phones[0] != '-':
            for phone in phones:
                phones_to_edit = phone.split('-')
                phones_to_delete = list(filter(None, phone.split(' ')))
                if len(phones_to_edit) == 2:
                    new_contact.edit_phone(phones_to_edit[0].strip(), phones_to_edit[1].strip())
                elif len(phones_to_delete) == 2 and phones_to_delete[0].strip() == "del":
                    new_contact.remove_phone(phones_to_delete[1].strip())
                else:
                    new_contact.add_phone(phone)
        
        if phones and phones[0] == '-':
            new_contact.remove_all_phones() 
        
        if email and email != '-':
            new_contact.edit_email(email)
        if email == '-':
            new_contact.remove_email()
        
        if address and address != '-':
            new_contact.edit_address(address)
        if address == '-':
            new_contact.remove_address()
        
        if birthday and birthday != '-':
            new_contact.edit_birthday(birthday)
        if birthday == '-':
            new_contact.remove_birthday()
        
        if name:
            self.address_book.edit_contact(contact.name.value, new_contact)
        print("Contact updated")
        

    def show_contacts(self):
        return self.address_book.show_contacts()

    def show_upcoming_birthdays(self, days):
        return self.address_book.show_upcoming_birthdays(days)

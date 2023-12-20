from models.contact import Contact, AddressBook

class ContactService:
    def __init__(self, address_book):
        self.address_book = address_book

    def add_contact(self, name, address=None, phones=None, emails=None, birthday=None):
        contact = Contact(name)
        if address:
            contact.address = AddressBook(address)
        if phones:
            for phone in phones:
                contact.add_phone(phone)
        if emails:
            for email in emails:
                contact.add_email(email)
        if birthday:
            contact.add_birthday(birthday)

        self.address_book.add_contact(contact)

    def find_contact(self, name):
        return self.address_book.find_contact(name)

    def delete_contact(self, name):
        self.address_book.delete_contact(name)

    def search_contacts(self, query):
        return self.address_book.search_contacts(query)

    def edit_contact(self, old_name, new_contact):
        self.address_book.edit_contact(old_name, new_contact)

    def show_contacts(self):
        return self.address_book.show_contacts()

    def show_upcoming_birthdays(self, days):
        return self.address_book.show_upcoming_birthdays(days)

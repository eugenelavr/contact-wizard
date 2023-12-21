from utils.validation_utils import ValidationUtils


def contact_input(add=True):
    if not add:
        old_name = input("Enter the name of the contact to edit: ").strip()
        while not old_name:
            old_name = input("Name is mandatory\nEnter the name of the contact to edit: ").strip()
    
    name = input("Enter name: ").strip()
    while not name:
        name = input("Name is mandatory\nEnter name: ").strip()
    
    if not add:
        pass # Edit phones if given in form <old> - <new>, <old1> - <new1>, ...
             # Rewrite phones if given in form <phone1>, <phone2>, ...

    phones = input("Enter phones (comma-separated): ").strip().split(",")
    while not ValidationUtils.validate_phone(phones):
        phones = input("Enter phones (comma-separated, optional): ").strip().split(",")
    
    email = input("Enter email (optional): ").strip()
    while not ValidationUtils.validate_email(email):
        email = input("Enter email (optional): ").strip()
    
    address = input("Enter address (optional): ").strip()
    
    birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
    while not ValidationUtils.validate_birthday(birthday):
        birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
    
    return {"name" : name, "phones" : phones, "email" : email, "address" : address, "birthday" : birthday}
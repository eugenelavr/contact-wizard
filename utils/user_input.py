from utils.validation_utils import ValidationUtils
import re


def contact_input(add=True, name=None):

    if not add:
        name = input("Enter name: ").strip()
        while not name and add:
            name = input("Name is mandatory\nEnter name: ").strip()
    
    if not add:
        print(" * Enter '-' to delete old data" )
    explanation = "{:<35} {:<50}\n".format(" - Edit phones", "<old> - <new>, <old1> - <new1>, ...")
    explanation += "{:<35} {:<50}\n".format(" - Add phones", "<phone1>, <phone2>, ...")
    explanation += "{:<35} {:<50}\n".format(" - Remove phone", "del <phone1>, del <phone2>")
    explanation += "{:<35} {:<50}".format(" - Combinations are supported", "<add_phone>, del <del_phone>, <old_phone> - <new_phone>")

    if not add:
        print(explanation)

    phones = input("Enter phones (comma-separated): ").strip().split(',')
    if add:
        if not ValidationUtils.validate_phone(phones):
            phones = input("Enter phones (comma-separated, optional): ").strip().split(",")
    else:
        if phones and phones != '-':
            for phone in phones:
                del_edit_phones = list(filter(None, re.split(r'[- ]|del', phone)))
                if not ValidationUtils.validate_phone(del_edit_phones):
                    phones = input("Enter phones (comma-separated, optional): ").strip().split(",")

    
    email = input("Enter email (optional): ").strip()
    while not ValidationUtils.validate_email(email) and email != '-':
        email = input("Enter email (optional): ").strip()
    
    address = input("Enter address (optional): ").strip()
    
    birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
    while not ValidationUtils.validate_birthday(birthday) and birthday != '-':
        birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
    
    return {"name" : name, "phones" : phones, "email" : email, "address" : address, "birthday" : birthday}
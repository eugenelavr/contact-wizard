import re
from datetime import datetime

class ValidationUtils:
    @staticmethod
    def validate_phone_list(phone_list):
        for i, phone in enumerate(phone_list):
            if phone_list[i] == "":
                #print("User without phone.")
                return True
            # Remove spaces from each phone number
            phone_list[i] = phone.replace(" ", "")

            if not phone_list[i].isdigit() or len(phone_list[i]) != 10:
              print(f"Invalid phone: {phone_list[i]}. Please enter a 10-digit number.")
              return False

        #print("All phones are valid.")
        return True

    @staticmethod
    def validate_email(email):
        if email == "":
            #print("User without email.")
            return True
        # Define a regular expression pattern for a basic email format
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Check if the email matches the pattern
        if re.match(pattern, email):
            return True
        else:
            print("Invalid email. Please enter a valid email.")
            return False
    
    @staticmethod
    def validate_birthday(birthday):
        if birthday == "":
            #print("User birthday empty.")
            return True
        try:
            # Parse the input string into a datetime object
            date_object = datetime.strptime(birthday, '%d.%m.%Y')
            return True
        except ValueError:
            print("Invalid birthday. Please enter a valid date DD.MM.YYYY.")
            # If parsing fails, it's not a valid date
            return False

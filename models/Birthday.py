from models.Field import Field

class Birthday(Field):
    def __init__(self, value):
        # try:
        #     datetime.strptime(value, '%d.%m.%Y')
        # except ValueError:
        #     raise ValueError("Invalid birthday format. Please use DD.MM.YYYY.")
        super().__init__(value)
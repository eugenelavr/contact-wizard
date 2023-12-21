from models.Field import Field
from datetime import datetime

# class Birthday(Field):
#     def __init__(self, value):
#         # try:
#         #     datetime.strptime(value, '%d.%m.%Y')
#         # except ValueError:
#         #     raise ValueError("Invalid birthday format. Please use DD.MM.YYYY.")
#         super().__init__(value)

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
import re

class FieldTypeHelper():
    @staticmethod
    def is_email(field_type):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', field_type):
            return False
        else:
            return True

    @staticmethod
    def is_phone(field_type):
        if not re.match(r'/^(?:\(\d{3}\)|\d{3}-)\d{3}-\d{4}$/', field_type):
            return False
        else:
            return True


    @staticmethod
    def is_date(field_type):
        return True


class FieldTypes():
    email = 'email'
    phone = 'phone'
    date = 'date'
    text = 'text'

    @staticmethod
    def get_type(field_value):
        if FieldTypeHelper.is_email(field_value):
            return FieldTypes.email
        elif FieldTypeHelper.is_phone(field_value):
            return FieldTypes.phone
        elif FieldTypeHelper.is_date(field_value):
            return FieldTypes.date
        else:
            return FieldTypes.text

from django.core.exceptions import ValidationError


def national_code(value):
    if len(value) != 10:
        raise ValidationError("Invalid National Code")
    if value == value[0] * 10:
        raise ValidationError("Invalid National Code")
    check = sum(int(value[i]) * (10 - i) for i in range(9)) % 11
    if check < 2 and check == int(value[9]):
        return True
    if check >= 2 and 11 - check == int(value[9]):
        return True


def phone_number(value):
    if len(value) != 11:
        raise ValidationError("Phone Number Must Be Exactly 11 characters Long")
    if not value.startswith("09"):
        raise ValidationError("Phone Number Must start With '09'")
    if not value[2:].isdigit():
        raise ValidationError("Phone Number Must Contain Only Numerical Digits")


def birth_date(value):
    if value.year > 2007:
        raise ValidationError("Birth Date Cannot Be Earlier Than 2007")

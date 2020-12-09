import datetime
from django.core.exceptions import ValidationError


def validate_birth_date(value):
    if value >= datetime.now().date():
        raise ValidationError('Birth date cannot be later today')
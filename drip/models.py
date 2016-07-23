from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
REMINDER_MODE = (
    (1, 'email'),
    (2, 'phone')
    )

class User(models.Model):
    email = models.EmailField(null=True, blank=True, unique=True)
    phone = models.CharField(max_length=10, null=True, blank=True, unique=True, validators=[
                             MinLengthValidator(10)])

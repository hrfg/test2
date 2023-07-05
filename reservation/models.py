from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.


def validate_positive(value):
    if value <= 0:
        raise ValidationError("Value must be more than 0.")


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(
        validators=[validate_positive, MaxValueValidator(6)])
    booking_date = models.DateField()

    def __str__(self):
        return f"ID:{self.id} - {self.name}"


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[validate_positive])
    inventory = models.IntegerField(
        validators=[validate_positive, MaxValueValidator(5)])

    def __str__(self):
        return f"ID:{self.id} - {self.title}"

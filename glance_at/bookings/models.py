from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    number_of_guests = models.PositiveBigIntegerField()
    booking_date = models.DateField()
    booking_date = models.TimeField()


    def __str__(self):
        return f"{self.name} - {self.booking_date} at {self.booking_time}"
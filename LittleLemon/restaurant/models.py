from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name
    


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
    def __str__(self):
        return f"{self.title} : {self.price}"
    


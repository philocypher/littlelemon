from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateField()
    
    def __str__(self) -> str:
        return f"Name: {self.name}, Number of guests: {self.no_of_guests}, Date: {self.bookingDate}"
        
        
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self) -> str:
        return f"title: {self.title}, price: {self.price}, inventory: {self.inventory}"
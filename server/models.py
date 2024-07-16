from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class User(models.Model):
    userID = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    work_email = models.EmailField()
    address = models.CharField(max_length=255)
    
class Store(models.Model):
    storeID = models.CharField(max_length=255)
    storeName = models.CharField(max_length=255)
    layout = models.CharField(max_length=50, choices=[
        ('aisle', 'Aisle'), 
        ('grid', 'Grid'), 
        ('free_flow', 'Free Flow')
    ])

class Vendor(models.Model):
    vendorID = models.CharField(max_length=255)
    vendorName = models.CharField(max_length=255)
    contactPerson = models.CharField(max_length=255, default=None)
    vendorAddress = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=13, default=None)
    vendorEmail = models.EmailField(default=None)

class Item(models.Model):
    itemID = models.CharField(max_length=255)
    vendorID = models.ForeignKey(Vendor.vendorID, on_delete=models.RESTRICT)
    itemName = models.CharField(max_length=255)
    itemUnit = models.CharField(max_length=100, choices=[
        #add item unit measurement
    ])
    itemPrice = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0.01), MaxValueValidator(99999.99)])
    itemCatID = models.ForeignKey(Category.catID, on_delete=models.PROTECT)
    itemDimensions = models

class Request(models.Model):
    requestID = models.CharField(max_length=255)
    userID = models.ForeignKey(User.userID, on_delete=models.RESTRICT)


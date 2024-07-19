from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class User(models.Model):
    userID = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    work_email = models.EmailField(default=None)
    address = models.CharField(max_length=255)
    
class Store(models.Model):
    storeID = models.CharField(max_length=255, primary_key=True)
    storeName = models.CharField(max_length=255)
    layout = models.CharField(max_length=50, choices=[
        ('aisle', 'Aisle'), 
        ('grid', 'Grid'), 
        ('free_flow', 'Free Flow')
        #add more layout options 
    ])
    storeLocation = models.CharField(max_length=255)

class Vendor(models.Model):
    vendorID = models.CharField(max_length=255, primary_key=True)
    vendorName = models.CharField(max_length=255)
    contactPerson = models.CharField(max_length=255, default=None)
    vendorAddress = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=13, default=None)
    vendorEmail = models.EmailField(default=None)

class Category(models.Model):
    catID = models.CharField(max_length=255, primary_key=True)
    catName = models.CharField(max_length=255)
    catType = models.CharField(max_length=50, choices=[
        #add category types here
    ])

class Item(models.Model):
    itemID = models.CharField(max_length=255, primary_key=True)
    vendorID = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name= 'vendors')
    itemName = models.CharField(max_length=255)
    itemUnit = models.CharField(max_length=100, choices=[
        #add item unit measurement tuples
    ])
    itemPrice = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0.01), MaxValueValidator(99999.99)])
    itemCatID = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category')
    minLevel = models.IntegerField(validators=[MinValueValidator(0)])

class Request(models.Model):
    requestID = models.CharField(max_length=255, primary_key=True)
    requestUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    requestDate = models.DateField(auto_now_add=True)
    requestReason = models.TextField(blank=True, help_text="Specify the reason for the request")
    requestStatus = models.CharField(max_length=255, choices=[
        #add request status tuples
    ])
    #Add this attribute after creating the approval model
    # Denied = models.CharField(default='No',choices=[
    #     ('True','Yes'),
    #     ('False', 'No')
    # ])
    #DeniedBy
    
class RequestDetails(models.Model):
    requestID = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='request')
    itemID = models.ForeignKey(Item, on_delete= models.RESTRICT, related_name='item')
    quantity = models.IntegerField(default= 0, validators=[MinValueValidator(0)])
    ExpectedPrice = models.IntegerField(default=0, validators=[MinValueValidator(0)])

class PurchaseRequest(models.Model):
    PurchaseRequestID = models.CharField(max_length=255, primary_key=True)
    AuthorizedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Approver')
    requestDate = models.DateField(auto_now_add=True)
    requestReason = models.TextField(blank=True, help_text="Specify the reason for the request")
    requestStatus = models.CharField(max_length=255, choices=[
        #add request status tuples
    ])
    AuthorizedDate = models.DateField(auto_now_add=True)
    ExpectedDeliveryDate = models.DateField(editable=True, null=True, blank=False)


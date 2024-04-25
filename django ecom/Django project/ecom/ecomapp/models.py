from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES=[(1,'Mobiles'),(2,'Clothes'),(3,'Shoes')]
    name=models.CharField(max_length=100)
    price=models.FloatField()
    pdetails=models.CharField(max_length=300)
    category=models.IntegerField(choices=CATEGORY_CHOICES)
    is_active=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to='images')




# CATEGORY_CHOICES converted to dictionary using list comprehension
# category_dict = {key: value for key, value in CATEGORY_CHOICES}
# print(category_dict)

# Initialize an empty dictionary
# category_dict = {}

# Populate the dictionary using a loop
# for key, value in CATEGORY_CHOICES:
#     category_dict[key] = value

# print(category_dict)
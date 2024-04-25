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



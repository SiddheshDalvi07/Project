from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    emailid = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=15)
    unit = models.CharField(max_length=10)
    date1 = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=15)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images')
    contact = models.CharField(max_length=15)
    emailid = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    plan = models.CharField(max_length=50)
    joindate = models.CharField(max_length=50)
    expiredate = models.CharField(max_length=50)
    initialamount = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    


class Trainer(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images')
    is_staff = models.BooleanField(default=True)
    contact = models.CharField(max_length=15)
    emailid = models.CharField(max_length=50)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    salary = models.IntegerField()
    experience = models.CharField(max_length=20)
    password = models.CharField(max_length=128)  # For storing the hashed password

    def __str__(self):
        return self.name



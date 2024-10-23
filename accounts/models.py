from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return  self.first_name + " " + self.last_name


class Product(models.Model):
    name = models.CharField(max_length=50),
    price = models.IntegerField(),
    stock = models.IntegerField(),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True),
    category = models.CharField(max_length=50),


    def __str__(self):
        return self.name + " " + self.price


class Customer(models.Model):
    first_name = models.CharField(max_length=50),
    last_name = models.CharField(max_length=50),
    email = models.EmailField(max_length=254),
    phone_number = models.CharField(max_length=14),

    def __str__(self):
        return self.first_name + " " + self.last_name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE),

    def __str__(self):
        return str(self.id)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE),


from django.db import models


class Person(models.Model):
    name  = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'name: {self.name}, phone: {self.phone}, address: {self.address}'


class Product(models.Model):
    name = models.CharField(max_length=40)
    product_info = models.CharField(max_length=100)

    def __str__(self):
        return f'name: {self.name}, type: {self.product_info}'


class Transaction(models.Model):
    person  = models.ForeignKey(Person, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count   = models.IntegerField()
    date  = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return f'person: {self.person}, product: {self.product}, count: {self.count}'

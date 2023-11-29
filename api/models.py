from django.db import models

# Create your models here.

class Rol(models.Model):
    idRol = models.IntegerField(primary_key=True,db_column="idRol")
    nameRol = models.CharField(max_length=100,db_column="nameRol")
    class Meta:
        db_table = "roles"

class Gender(models.Model):
    idGender = models.IntegerField(primary_key=True,db_column="idGender")
    nameGender = models.CharField(max_length=100,db_column="nameGender")
    class Meta:
        db_table = "genders"

class Profile(models.Model):
    idUser = models.IntegerField(primary_key=True,db_column="idUser")
    nameUser = models.CharField(max_length=100,db_column="nameUser")
    emailUser = models.EmailField(unique=True,db_column="emailUser")
    passwordUser = models.CharField(max_length=255,db_column="passwordUser")
    class Meta:
        db_table = "profiles"

class Product(models.Model):
    idProduct = models.IntegerField(primary_key=True,db_column="idProduct")
    nameProduct = models.CharField(max_length=100,db_column="nameProduct")
    priceProduct = models.FloatField(default=0,db_column="priceProduct")
    class Meta:
        db_table = "products"
        
class Question(models.Model):
    id = models.IntegerField(primary_key=True,db_column="id")
    name = models.CharField(max_length=100,db_column="name")
    lastName = models.CharField(max_length=100,db_column="lastName")
    email = models.CharField(max_length=100,db_column="email")
    package = models.CharField(max_length=100,db_column="package")
    person = models.CharField(max_length=100,db_column="person")
    packaging = models.CharField(max_length=100,db_column="packaging")
    reasonPurchase = models.CharField(max_length=100,db_column="reason_purchase")
    send = models.CharField(max_length=100,db_column="send")
    mark = models.CharField(max_length=100,db_column="mark")
    category = models.CharField(max_length=100,db_column="category")
    article = models.CharField(max_length=100,db_column="article")
    class Meta:
        db_table = "questions"

class Order(models.Model):
    product = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'{self.product} - ${self.amount}'

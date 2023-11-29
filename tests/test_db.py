import pytest
from django.db.utils import IntegrityError
from api.models import *

@pytest.mark.django_db
def test_create_rol():
    rol = Rol.objects.create(idRol=1, nameRol="Admin")
    assert rol.idRol == 1
    assert rol.nameRol == "Admin"

@pytest.mark.django_db
def test_create_gender():
    gender = Gender.objects.create(idGender=1, nameGender="Male")
    assert gender.idGender == 1
    assert gender.nameGender == "Male"

@pytest.mark.django_db
def test_create_profile():
    profile = Profile.objects.create(idUser=1, nameUser="John", emailUser="john@example.com", passwordUser="password")
    assert profile.idUser == 1
    assert profile.nameUser == "John"
    assert profile.emailUser == "john@example.com"
    assert profile.passwordUser == "password"

@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(idProduct=1, nameProduct="Laptop", priceProduct=999.99)
    assert product.idProduct == 1
    assert product.nameProduct == "Laptop"
    assert product.priceProduct == 999.99

@pytest.mark.django_db
def test_create_question():
    question = Question.objects.create(id=1, name="John", lastName="Doe", email="john.doe@example.com",
                                       package="Package1", person="Person1", packaging="Packaging1",
                                       reasonPurchase="Reason1", send="Yes", mark="Mark1",
                                       category="Category1", article="Article1")
    assert question.id == 1
    assert question.name == "John"
    assert question.lastName == "Doe"
    assert question.email == "john.doe@example.com"
    assert question.package == "Package1"
    assert question.person == "Person1"
    assert question.packaging == "Packaging1"
    assert question.reasonPurchase == "Reason1"
    assert question.send == "Yes"
    assert question.mark == "Mark1"
    assert question.category == "Category1"
    assert question.article == "Article1"

@pytest.mark.django_db
def test_create_order():
    order = Order.objects.create(product="Laptop", amount=999.99)
    assert str(order) == "Laptop - $999.99"

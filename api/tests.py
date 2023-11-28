from django.test import TestCase

# Create your tests here.
from .models import *

class RolTest(TestCase):
    def setUp(self):
        self.rol = Rol.objects.create(idRol=1, nameRol="Admin")

    def test_rol_name(self):
        self.assertEqual(self.rol.nameRol, "Admin")

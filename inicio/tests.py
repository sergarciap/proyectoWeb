
from django.test import TestCase
from .models import Formulario
import pytest
import pytest_html

# Create your tests here.
# registro de formulario

class FormularioTestCase(TestCase):
    def setUp(self):
        Formulario.objects.create(rut="123456",nombre="Matt d",correo="lowis@hotmail.com",telefono="97142992",mensaje="planes porfavor",edad="28",sexo="hombre",comuna="viña del mar")

    def test_crear_formulario(self):
        form1=Formulario.objects.get(id=1)
        field_label = form1._meta.get_field("rut").verbose_name
        self.assertEquals(field_label,"rut")

    def test_obtener_label(self):
        form2=Formulario.objects.get(id=1)
        field_label = form2._meta.get_field('correo').verbose_name
        self.assertEquals(field_label,"correo")

from django.forms import ModelForm
from .models import Formulario
from django import forms


class FormularioForm(forms.ModelForm):
     class Meta:
        model = Formulario
        comunas = [("viñadelmar", "viña del mar"),
                    ("valparaiso", "valparaiso"), ("santiago", "Santiago"), ("temuco", "Temuco"), ("concepcion", "Concepción")]
        sexos=[("hombre", "hombre"), ("mujer", "mujer")]
        fields=['rut', 'nombre', 'correo', 'telefono',
            'mensaje', 'edad', 'sexo', 'comuna']
        widgets={
            'rut': forms.TextInput(attrs={'class': 'form-control clas', 'placeholder': 'Rut'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control clas', 'placeholder': 'Nombre'}),
            'correo': forms.TextInput(attrs={'type': 'email', 'class': 'form-control clas', 'placeholder': 'correo'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control clas'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control clas', 'placeholder': 'Mensaje  '}),
            'edad': forms.TextInput(attrs={'class': 'form-control clas', 'placeholder': 'edad  '}),
            'sexo': forms.RadioSelect(choices=sexos, attrs={'class': 'classs radio-button ', 'placeholder': 'sexo  '}),
            'comuna':forms.Select(choices=comunas,attrs={'class': 'clas', 'placeholder': 'comuna  '})
        }
      

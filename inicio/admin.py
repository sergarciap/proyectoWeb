from django.contrib import admin
from .models import Post,Entrenamiento,Formulario, Karate
from login.models import Profile
#importando modelos en la pagina del admin
admin.site.register(Entrenamiento)

admin.site.register(Post)

admin.site.register(Karate)

admin.site.register(Profile)

admin.site.register(Formulario)


#*****************************************************************************************

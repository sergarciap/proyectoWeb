from django.urls import path,include
from . import views
from django.conf import settings
from .views import  PageUpdate, PageDelete
from django.contrib.auth.views import LogoutView
from django.conf.urls import include, url

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logoutt"),
    path('', views.base, name="Base"),
    path('home', views.inicio, name="inicio"),
    path('Karate/', views.karate, name='Karate'),
    path('Entrenamiento/', views.entrenamiento, name="Entrenamiento"),
    path('Formulario/', views.FormularioPost, name='Formulario'),
    path('form-list/', views.PageList.as_view(), name='Formulario-Lista'),
    path('form-list/<int:pk>/', views.entrenamientoList, name='Formulario-List'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('login.urls')),
    path('update/<int:pk>/', views.PageUpdate.as_view(),name='update'),
    path('delete/<int:pk>/', views.PageDelete.as_view(),name='delete'),

]
#*****************************************************************************************
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

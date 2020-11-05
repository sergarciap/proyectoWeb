from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from .models import  Entrenamiento, Post, Formulario, Karate
from .forms import FormularioForm
from django.http import HttpResponse
# Create your views here.
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, PermissionRequiredMixin
from django.contrib.auth import logout
from django.template import loader

#primera vista
class LogoutIfNotStaffMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            logout(request)
            return self.handle_no_permission()
        return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)


class HomePageView(PermissionRequiredMixin, LogoutIfNotStaffMixin, TemplateView):
    template_name = "inicio/inicio.html"
    permission_required = ['is_staff', 'is_user']

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class EntrenamientoPageView(TemplateView):
    template_name = "inicio/Entrenamiento.html"


class FormularioPageView(TemplateView):
    template_name = "inicio/Formulario.html"


class KaratePageView(TemplateView):
    template_name = "Inicio/Karate.html"

@login_required
def inicio(request):
    return render(request, "inicio/inicio.html")


class BasePageView(PermissionRequiredMixin, LogoutIfNotStaffMixin, TemplateView):
    template_name = "Inicio/base.html"
    permission_required = ['is_staff', 'is_user']


@login_required
def base(request):
    return render(request, "Inicio/base.html")



@login_required
def FormularioPost(request):
    units = Formulario.objects.all()
    if request.method == 'POST':
        if request.POST.get('rut') and request.POST.get('mensaje'):

            rut = request.POST.get('rut')
            nombre = request.POST.get('nombre')
            correo = request.POST.get('email')
            telefono = request.POST.get('telefono')
            mensaje = request.POST.get('mensaje')
            edad = request.POST.get('edad')
            sexo = request.POST.get('sexo')
            comuna = request.POST.get('comuna')
            p = Formulario(rut=rut, nombre=nombre, correo=correo,
                           telefono=telefono, edad=edad, comuna=comuna, sexo=sexo, mensaje=mensaje)
            p.save()
            return render(request, "inicio/Formulario.html", {'list': units})

    else:
        return render(request, "inicio/Formulario.html")


@login_required
def entrenamiento(request):
    training = get_object_or_404(Entrenamiento, id=1)
    training1 = get_object_or_404(Entrenamiento, id=2)
    training2 = get_object_or_404(Entrenamiento, id=3)
    return render(request, "inicio/Entrenamiento.html", {'training': training, 'training1': training1, 'training2': training2})

@login_required
def karate(request):
    karate = get_object_or_404(karate, id=1)
    return render(request, "Inicio/Karate.html", {'karate': karate})

@login_required
def entrenamientoList(request, pk):
    template = loader.get_template('Inicio/formularios_list.html')
    context = {
        'list': Formulario.objects.all(),
    }
    return HttpResponse(template.render(context, request))


@login_required
def entrenamientoListSinPk(request):
    template = loader.get_template('Inicio/formularios_list.html')
    context = {
        'list': Formulario.objects.all(),
    }
    return HttpResponse(template.render(context, request))


class PageList(PermissionRequiredMixin, LogoutIfNotStaffMixin, TemplateView):
    model = Formulario
    permission_required = 'is_staff'
    units = Formulario.objects.all()
    template_name = "Inicio/formularios_list.html"

    def get(self, request, *args, **kwargs):
        units = Formulario.objects.all()
        return render(request, self.template_name, {'list': units})


class PageUpdate(PermissionRequiredMixin, LogoutIfNotStaffMixin, UpdateView):
    model = Formulario
    form_class = FormularioForm
    template_name_suffix = '_update_form'
    permission_required = 'is_staff'

    def get_success_url(self):
        return reverse_lazy('Formulario-List', args=[self.object.id]) + '?ok'


class PageDelete(PermissionRequiredMixin, LogoutIfNotStaffMixin, DeleteView):
    model = Formulario
    permission_required = 'is_staff'

    def get_success_url(self):
        return reverse_lazy('Formulario-List', args=[self.object.id]) + '?ok'

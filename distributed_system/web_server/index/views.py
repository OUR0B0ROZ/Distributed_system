from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import ModelTest
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from allauth.account.views import LoginView, LogoutView, SignupView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
    )
from django.http import HttpResponseRedirect
# Create your views here.


#class IndexView(TemplateView):
#   template_name = 'index/index.html'

class InitPageView  (ListView,):
    model = ModelTest  # Set the model to 'ModelTest'
    template_name = 'index/init.html'  # Specify the template for the list view
    context_object_name = 'init'  # Name of the variable to use in the template

class CustomLoginView(LoginView):
    template_name = 'index/login.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            # Si el usuario ya está autenticado, redirigir a la página de inicio de sesión
            return redirect('index:login')
        return super().get(*args, **kwargs)

class CustomLogoutView(LogoutView):
    template_name = 'index/logout.html'

class ModelListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ModelTest
    template_name = 'index/model_list.html'
    context_object_name = 'model_list'
    permission_required = 'index.view_modeltest'
    
class ModelDetailView(DetailView):
    model = ModelTest  # Set the model to 'ModelTest'
    template_name = 'index/model_detail.html'  # Specify the template for the detail view
    context_object_name = 'model'  # Name of the variable to use in the template

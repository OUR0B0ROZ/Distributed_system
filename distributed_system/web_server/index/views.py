from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import ModelTest
from django.views.generic import DetailView
# Create your views here.


#class IndexView(TemplateView):
#   template_name = 'index/index.html'

class ModelListView(ListView):
    model = ModelTest  # Set the model to 'ModelTest'
    template_name = 'index/model_list.html'  # Specify the template for the list view
    context_object_name = 'model_list'  # Name of the variable to use in the template
    
class ModelDetailView(DetailView):
    model = ModelTest  # Set the model to 'ModelTest'
    template_name = 'index/model_detail.html'  # Specify the template for the detail view
    context_object_name = 'model'  # Name of the variable to use in the template

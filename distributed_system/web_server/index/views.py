from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import ModelTest
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse,reverse_lazy
# Create your views here.


#class IndexView(TemplateView):
#   template_name = 'index/index.html'

class ModelListView(ListView):
    model = ModelTest  # Set the model to 'ModelTest'
    template_name = 'index/model_list.html'  # Specify the template for the list view
    context_object_name = 'model'  # Name of the variable to use in the template
    
class ModelDetailView(DetailView):
    model = ModelTest  # Set the model to 'ModelTest'
    template_name = 'index/model_detail.html'  # Specify the template for the detail view
    context_object_name = 'model'  # Name of the variable to use in the template
    


class ModelTestCreateView(CreateView):
    model = ModelTest
    template_name = 'index/modeltest_form.html'  # Create a template for the creation form
    fields = ['autor', 'category', 'title', 'slug', 'body']
  
    def get_success_url(self):
        # Ensure you use the correct URL name defined in your urls.py
        return reverse('index:detail', args=[str(self.object.pk)])

class ModelTestUpdateView(UpdateView):
    model = ModelTest
    template_name = 'index/modeltest_form.html'  # Replace with your template path
    fields = ['autor', 'category', 'title', 'slug', 'body']
    

class ModelTestDeleteView(DeleteView):
    model = ModelTest
    template_name = 'index/modeltest_confirm_delete.html'  # Replace with your template path
    success_url = reverse_lazy('index:model-list')  # Redirect to a list view after deletion
    

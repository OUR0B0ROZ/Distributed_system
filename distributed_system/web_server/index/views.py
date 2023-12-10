from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import ModelTest,Category
from django.views.generic import DetailView
# Create your views here.


#class IndexView(TemplateView):
#   template_name = 'index/index.html'

class ModelListView(ListView):
    model = ModelTest  # Set the model to 'ModelTest'
    template_name = 'index/model_list.html'  # Specify the template for the list view
    context_object_name = 'model_list'  # Name of the variable to use in the template
    
    def get_queryset(self):
        sort_option = self.request.GET.get('sort_option', 'numerical')
        category_filter = self.request.GET.get('category_filter')

        queryset = ModelTest.objects.all()

        if category_filter:
            queryset = queryset.filter(category__slug=category_filter)

        if sort_option == 'numerical':
            queryset = sorted(queryset, key=lambda x: (x.creation_year, x.initial, x.title))
        elif sort_option == 'alphabetical':
            queryset = sorted(queryset, key=lambda x: (x.initial, x.title, x.creation_year))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_option'] = self.request.GET.get('sort_option', 'numerical')
        context['category_filter'] = self.request.GET.get('category_filter')
        context['categories'] = Category.objects.all()

          # Set the selected category
        context['selected_category'] = (
            Category.objects.get(slug=context['category_filter'])
            if context['category_filter']
            else None
        )
        return context

class ModelDetailView(DetailView):
    model = ModelTest  # Set the model to 'ModelTest'
    template_name = 'index/model_detail.html'  # Specify the template for the detail view
    context_object_name = 'model'  # Name of the variable to use in the template


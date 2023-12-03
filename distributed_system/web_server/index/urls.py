from django.urls import path
from .views import ModelListView, ModelDetailView ,CustomLoginView, CustomLogoutView,InitPageView,RedirectView 

app_name = 'index'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
 
    path('',InitPageView .as_view(), name='initpage'),
    path('index/', ModelListView.as_view(), name='model-list'),
    path('redirect/', RedirectView.as_view(), name='redirect'),
    path('<slug:slug>/', ModelDetailView.as_view(), name='model-detail'),  # Ensure that the name is 'model-detail'
   
]

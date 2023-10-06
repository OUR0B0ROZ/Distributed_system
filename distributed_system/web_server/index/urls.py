from django.urls import path
from .views import ModelListView, ModelDetailView

app_name = 'index'

urlpatterns = [
    path('', ModelListView.as_view(), name='model-list'),
    path('<slug:slug>/', ModelDetailView.as_view(), name='detail'),  # Ensure that the name is 'model-detail'
]

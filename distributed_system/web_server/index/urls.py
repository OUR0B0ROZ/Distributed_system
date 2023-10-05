from django.urls import path
from .views import IndexView,ModelDetailView

app_name = 'index'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
     path('<slug:slug>/', ModelDetailView.as_view(), name='model-detail'),
]
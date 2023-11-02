from django.urls import path
from .views import ModelListView, ModelDetailView, ModelTestCreateView,ModelTestUpdateView,ModelTestDeleteView

app_name = 'index'

urlpatterns = [
    path('', ModelListView.as_view(), name='model-list'),
    path('<int:pk>/', ModelDetailView.as_view(), name='detail'),
    path('create/', ModelTestCreateView.as_view(), name='modeltest-create'),
    path('<int:pk>/update/', ModelTestUpdateView.as_view(), name='modeltest-update'),
    path('<int:pk>/delete/', ModelTestDeleteView.as_view(), name='modeltest-delete'),


]

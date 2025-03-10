from django.urls import path
from .views import training_list, add_training, edit_training, delete_training
from training.views import training_list, add_training, edit_training, delete_training


urlpatterns = [
    path('', training_list, name='training_list'),
    path('add/', add_training, name='add_training'),
    path('edit/<int:training_id>/', edit_training, name='edit_training'),  
    path('delete/<int:training_id>/', delete_training, name='delete_training'),
]

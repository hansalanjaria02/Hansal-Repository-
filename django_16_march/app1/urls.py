from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),          # Home page (List)
    path('add/', views.student_create, name='student_create'),  # Naya student
    path('edit/<int:pk>/', views.student_update, name='student_update'), # Edit
    path('delete/<int:pk>/', views.student_delete, name='student_delete'), # Delete
]
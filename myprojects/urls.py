from django.urls import path
from . import views



urlpatterns = [
    path('', views.projects, name = 'projects'),
    path('project/<str:pk>/', views.project, name = 'project'),
    path('project_form/', views.project_form, name = 'project_form'),
    path('update_project/<str:pk>/', views.update_project, name = 'update_project'),
    path('delete_project/<str:pk>/', views.delete_project, name = 'delete_project'),
] 

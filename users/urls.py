from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name = 'profiles'),
    path('profile/<str:pk>/', views.profile, name = 'profile'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('account/', views.user_account, name = 'user_account'),
    path('account_form/', views.edit_account_form, name = 'edit_account_form'),
    path('skill_form', views.skill_form, name = 'skill_form'),
    path('update_skill_form/<str:pk>/', views.update_skill_form, name = 'update_skill_form'),
    path('delete_skill/<str:pk>/', views.delete_skill, name = 'delete_skill'),
    path('inbox/', views.inbox, name = 'inbox'),
    path('message/<str:pk>/', views.view_message, name = 'message'),
    path('create_message/<str:pk>/', views.create_message, name = 'create_message')
]

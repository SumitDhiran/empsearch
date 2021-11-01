from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),

    path('',views.candidates,name='candidates'),
    path('candidate-add/', views.addCandidate,name='candidate-add'),
    path('candidate-update/<str:pk>/', views.updateCandidate, name='candidate-update'),
    path('candidate-delete/<str:pk>/', views.deleteCandidate, name='candidate-delete'),


]

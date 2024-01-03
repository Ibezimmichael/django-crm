from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name=""),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("create-customer", views.create_customer, name="create-customer"),
    path("update-customer/<int:pk>", views.update_customer, name="update-customer"),
    path("view-customer/<int:pk>", views.single_customer, name="single-customer"),
    
]

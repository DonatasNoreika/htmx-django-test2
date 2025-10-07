from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts, name="contacts"),
    path('search/', views.search, name="search"),
    path('contacts/<int:contact_id>/delete', views.delete_contact, name="delete_contact"),
]

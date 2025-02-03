from django.urls import path
from .views import landing,contact

urlpatterns = [
    path('landing/', landing, name='landing'),
    path('contact/',contact,name="contact")
]

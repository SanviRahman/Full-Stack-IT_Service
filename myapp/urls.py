from django.urls import path
from .views import landing,contact,service

urlpatterns = [
    path('landing/', landing, name='landing'),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
]

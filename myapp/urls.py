from django.urls import path
from .views import service,serviceDetails,about

urlpatterns = [
    # path('landing/', landing, name='landing'),
    # path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
    path('serviceDetails/<int:pk>/',serviceDetails,name='serviceDetails'),
    path('about/', about, name='about'),
]

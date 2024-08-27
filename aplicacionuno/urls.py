from django.urls import path
from aplicacionuno.views import *

urlpatterns = [
    path('', home, name='home'), 
    path('about/', about, name='about'), 
    path('contact/', contact, name='contact'), 
    path('services/', services, name='services'),
    path('registro/', showformdata, name='registro'),
    path('viewdata/', viewdata, name='viewdata'),
    path('editpropietario/<int:id>/', Editpropietario, name='editpropietario'),
    path('update/<int:id>/', updateprop, name='updateprop'),
    path('deletepropietario/<int:id>/', deletepropietario, name='deletepropietario'),
]


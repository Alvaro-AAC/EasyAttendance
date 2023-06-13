from django.urls import path

from .views import *

urlpatterns = [
    path('', redirecter),
    path('login/', login),
    path('clases/', home),
    path('verifyLogin/', verifyLogin),
    path('logout/', logout),
    path('crearclase/', crearclase),
    path('verificar/<token>/', verificar),
]

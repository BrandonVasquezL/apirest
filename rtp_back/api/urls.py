from django.urls import path
from . import views

urlpatterns = [
    ### URLS Reportes ###
    path('parking/', views.getParking),
    path('parking/post/', views.postParking),
    
]
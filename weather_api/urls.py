from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="home"),
     path("contact", views.contact, name="contact"),
      path('location/',views.location,name='location'),
    path("result", views.result, name="result"),
    
]

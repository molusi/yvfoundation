
from . import views
from .views import contact_view
from django.urls import path
from . models import *


app_name = "yvfoundation"

urlpatterns = [
    path('',views.yvfoundationhome,name='home'),
    path('contact/',contact_view,name="contact"),
    path('about/',views.AboutView.as_view(),name="about"),
    ]

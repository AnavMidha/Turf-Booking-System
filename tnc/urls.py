from django.urls import path
from . import views

urlpatterns=[
    path('tnc/',views.tnc,name="tnc")
]
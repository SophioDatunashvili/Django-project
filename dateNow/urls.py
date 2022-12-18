from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dateNow',views.current_datetime, name='date'),
]
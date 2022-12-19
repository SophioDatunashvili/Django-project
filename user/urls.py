from django.urls import path
from . import views


urlpatterns = [
    # path('User', views.userhome),
    path('', views.userform, name='form'),
    path('save/', views.saveform),
]
from django.urls import path
from . import views


urlpatterns = [
    # path('User', views.userhome),
    path('/form',views.userform, name="user"),
    path('save', views.saveform),
]
from django.urls import path
from app_cad_users import views

urlpatterns = [
    # rote, view response, name
    # users.com
    path('',views.home, name='home'),
]

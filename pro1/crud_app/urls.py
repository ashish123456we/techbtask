from django.urls import path
from . import views


urlpatterns = [
    path('lappy1/', views.laptop_create_view, name='add_url'),
    path('lappy/', views.laptop_retrive_view, name='retrive_url')

]

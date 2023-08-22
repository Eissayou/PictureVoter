from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('imagerate', views.imagerate, name = 'imagerate'),
    path('logout/',views.logout_user, name = 'logout'),
    path('register/',views.register_user, name = 'register'),
    path('draw/', views.draw_and_submit, name='draw_and_submit'),
]
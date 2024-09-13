from django.urls import path
from .views import login_view, logout_view, register_view, get_user_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('user/', get_user_view, name='get_user'),
]

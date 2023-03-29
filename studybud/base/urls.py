from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('room/<str:pk>', room, name='room'),
    path('create-room/', create_room, name='create-room'),
    path('update-room/<str:pk>/', updateroom, name='update-room'),
    path('delete-room/<str:pk>/', deleteroom, name='delete-room'),
    path('login/', loginpage, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('register/', register_user, name='register'),
    path('delete-message/<str:pk>/', deletemessage, name='delete-message'),
    path('update-user/', updateUser, name='update-user'),
    path('profile/<str:pk>/', userProfile, name='user-profile'),
]
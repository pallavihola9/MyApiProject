from django.urls import path
from .views import *



urlpatterns = [
    
   path('register/',RegisterUserPost.as_view(), name= 'register'),
   path('userdate/',UserDataGet.as_view(), name= 'userdata'),
   path('userdate/<int:pk>/',UserDataUpdateDelete.as_view(), name= 'userdate_put'),
   path('userdate/<int:pk>/',UserDataUpdateDelete.as_view(), name= 'userdate_delete'),

]
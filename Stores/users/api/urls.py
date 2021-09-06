from django.urls import path
from users.api.views import RegisterUser

urlpatterns = [
   path('register/',RegisterUser.as_view())
]
    


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include('products.api.urls')),
    # favorites/comments,para los comentarios
    path('favorites/',include('favorite_comments.api.urls')),
    path('',include('bills.api.urls')),

    # register user
    path('',include('users.api.urls'))
]
    

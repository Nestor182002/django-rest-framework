from django.db import router
from django.urls import path, include
# view
from products.api.views import ProductsView
# router
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'',ProductsView, basename='products')


urlpatterns = [  
   path('',include(router.urls))
]
  
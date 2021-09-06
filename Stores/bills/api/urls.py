from django.urls import path,include
from rest_framework.routers import DefaultRouter

from bills.api.views import BillsViewset

#router 
router=DefaultRouter()
router.register(r'bills',BillsViewset, basename='')


urlpatterns = [  
  # bills
   path('', include(router.urls)),
]
  
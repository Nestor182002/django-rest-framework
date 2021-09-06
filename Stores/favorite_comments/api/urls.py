from django.urls import path,include
from rest_framework.routers import DefaultRouter
# 
from favorite_comments.api.views import ProductsFavorite,ProductsFavoriteDetail, commentsViewset



router=DefaultRouter()
router.register(r'comments',commentsViewset, basename='')


urlpatterns = [  
   # favorites_products
   path('', ProductsFavorite.as_view()),
   path('<int:pk>/',ProductsFavoriteDetail.as_view()),


   # comments
   path('', include(router.urls)),
]
  
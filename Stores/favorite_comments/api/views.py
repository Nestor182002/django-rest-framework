from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status,viewsets
from django.http import Http404

# models
from  favorite_comments.models import Favorite, Comments
from  favorite_comments.api.serializers import ProductsSerializer,CommentsSerializer
# permisos
from  favorite_comments.api.permission import UserToUser




class ProductsFavorite(APIView):
    
    def get(self,request,format=None):
        favorite = Favorite.objects.filter(id_person=request.user)
        serializer = ProductsSerializer(favorite, many=True)
        return Response(serializer.data)
    # valido que no haya mas favoritos iguales
    def post(self, request, format=None):
        serializer = ProductsSerializer(data=request.data)
        product=request.data["id_products"]
        if Favorite.objects.filter(id_person=request.user,id_products=product).exists():
            return Response({"favorites":"favorites is already exists"}, status=status.HTTP_400_BAD_REQUEST)

        elif serializer.is_valid(raise_exception=True):
            serializer.save(id_person=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductsFavoriteDetail(APIView):
    permission_classes=[UserToUser,]
    def get_object(self, pk):
        try:
            obj=Favorite.objects.get(pk=pk)
            self.check_object_permissions(self.request,obj)
            return obj
        except Favorite.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductsSerializer(snippet)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        Favorite = self.get_object(pk)
        Favorite.delete()
        return Response({"eliminado"})

    def post(self, request, format=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class commentsViewset(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def update(self, request,pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_create(self, serializer):
        serializer.save(id_person=self.request.user)


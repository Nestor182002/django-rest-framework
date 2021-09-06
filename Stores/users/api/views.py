from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from users.api.serializers import RegisterUserSerializer



class RegisterUser(APIView):

    def post(self, request, format=None):
        serializer = RegisterUserSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"user created success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
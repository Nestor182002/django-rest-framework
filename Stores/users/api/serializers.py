from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('email','password','username','first_name','last_name')


    def validate(self, args):
        firstname=args.get('first_name','')
        lastname=args.get('last_name','')
        if firstname =='' or lastname =='':
            raise serializers.ValidationError({'name':('please complete the data')})
        email=args.get('email','') 
        username=args.get('username','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('username already exists')})
        return super().validate(args)

    def create(self, validated_data):
        user=User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    

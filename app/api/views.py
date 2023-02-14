from django.shortcuts import render,HttpResponse
from .serializers import blogser,likeser,userser
from . models import blog,likes
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser
# from rest_framework.generics import ListAPIView
# Create your views here.



# the owner of his blog only acces the data and do CRUD operations for him self with this API

# Thank you!..


class blog_api(viewsets.ModelViewSet):
    queryset=blog.objects.all()
    serializer_class=blogser
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user1=self.request.user
        
        print(user1)
        return blog.objects.filter(user=user1)

#The owner of his likes he can only acces and do CRUD operation for him self with this API

# Thank you!..


class likes_api(viewsets.ModelViewSet):
    queryset=likes.objects.all()
    serializer_class=likeser
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user1=self.request.user
        
        print(user1)
        return likes.objects.filter(user=user1)

#owner of the account can only access this api data and can do CRUD operation for him self with this API

# Thank you!..


class user_owner(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userser
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        pk=self.request.user

        return (User.objects.filter(username=pk))


#this is superuser alias ADMIN He have all accounts acces hhe can do anu CRUD operations with this API

# Thank you!..

class user_api(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userser
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAdminUser]
    # def get_queryset(self):
    #     user1=self.request.user
        
    #     print(user1)
    #     return User.objects.filter(user=user1)
        

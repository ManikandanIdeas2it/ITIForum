from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Postdata
from .serializer import UserSerializer, PostdataSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostdataViewSet(viewsets.ModelViewSet):
    queryset = Postdata.objects.all()
    serializer_class = PostdataSerializer
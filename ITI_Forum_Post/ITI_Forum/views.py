from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Users, Fourm_post
from .serializer import UsersSerializer, FourmPostSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


class FourmPostViewSet(viewsets.ModelViewSet):
    queryset = Fourm_post.objects.all()
    serializer_class = FourmPostSerializer
    permission_classes = [permissions.IsAuthenticated]

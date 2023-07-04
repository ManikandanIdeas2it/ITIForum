from rest_framework import serializers
from .models import User, Postdata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'emp_id', 'name', 'createdat', 'Createddate')

class PostdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postdata
        fields = ('postid', 'emp_id', 'text', 'image', 'categories', 'like', 'comment', 'caption', 'createdat', 'Createddate')

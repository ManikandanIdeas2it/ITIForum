from rest_framework import serializers
from .models import Users, Fourm_post


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'user_name', 'user_emp_id')


class FourmPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fourm_post
        fields = ('post_id', 'post_text', 'post_image', 'post_caption', 'User_user_id',
                  'Post_likes_like_id', 'Post_comment_comm_id')

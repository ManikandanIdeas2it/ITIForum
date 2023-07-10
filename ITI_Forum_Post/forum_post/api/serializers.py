from rest_framework import serializers
from forum_post.models import Users, PostsCollection

class PostsCollectionSerializer(serializers.ModelSerializer):
    emp_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    post_id = serializers.UUIDField(format="hex") 
    post_category = serializers.CharField() 
    post_text = serializers.CharField()
    post_img = serializers.ImageField()
    post_caption = serializers.CharField()
    like_fk = serializers.IntegerField()
    comment_fk = serializers.CharField()
    date_posted = serializers.DateTimeField()
    date_last_modified = serializers.DateTimeField()
    
    class Meta:
        model = PostsCollection
        fields = ('emp_id', 'post_id', 'post_category', 'post_text', 'post_img', 'post_caption', 'like_fk', 'comment_fk', 'date_posted', 'date_last_modified')

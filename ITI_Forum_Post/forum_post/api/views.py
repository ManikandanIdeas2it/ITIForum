from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from forum_post.models import Users, PostsCollection
from forum_post.api.serializers import PostsCollectionSerializer


class PostsCollectionAV(APIView):
    
    def get(self, request):
        all_posts = PostsCollection.objects.all()
        serializer = PostsCollectionSerializer(all_posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        pass
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass
    
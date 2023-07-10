# API urls for returning Data should be specified here

from django.urls import include, path
from forum_post.api.views import PostsCollectionAV


urlpatterns = [
    path('all/',PostsCollectionAV.as_view(), name='all_posts'),
]
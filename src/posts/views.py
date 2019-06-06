from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET'])
def likePost(request, *args, **kwargs):
    post = get_object_or_404(Post, id=kwargs['id'])
    request.user.like(post)
    return Response({"ok": "request finished!"})


@api_view(['GET'])
def unlikePost(request, *args, **kwargs):
    post = get_object_or_404(Post, id=kwargs['id'])
    request.user.unlike(post)
    return Response({"ok": "request finished!"})    
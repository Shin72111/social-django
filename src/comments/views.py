from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Comment


@api_view(['GET'])
def likeComment(request, *args, **kwargs):
    comment = get_object_or_404(Comment, id=kwargs['id'])
    request.user.like(comment)
    return Response({"ok": "request finished!"})


@api_view(['GET'])
def unlikeComment(request, *args, **kwargs):
    comment = get_object_or_404(Comment, id=kwargs['id'])
    request.user.unlike(comment)
    return Response({"ok": "request finished!"})

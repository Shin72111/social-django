from rest_framework import serializers
from comments.serializers import CommentSerializer
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'username',
            'body',
            'created_on',
            'comments'
        ]
        extra_kwrags = {
            'user': {'write_only': True}
        }



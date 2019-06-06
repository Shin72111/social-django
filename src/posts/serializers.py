from rest_framework import serializers
from comments.serializers import CommentSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    likes = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'username',
            'body',
            'likes',
            'created_on',
            'comments'
        ]
        extra_kwrags = {
            'user': {'write_only': True}
        }

    def get_likes(self, obj):
        return obj.liked.all().count()

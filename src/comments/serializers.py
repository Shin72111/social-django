from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'username',
            'post',
            'body',
            'likes',
            'created_on'
        ]
        extra_kwargs = {
            'user': {'write_only': True},
            'post': {'write_only': True}
        }

    def get_likes(self, obj):
        return obj.liked.all().count()

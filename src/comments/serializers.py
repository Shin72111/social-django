from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    likes = serializers.SerializerMethodField()
    was_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'username',
            'post',
            'body',
            'likes',
            'was_liked',
            'created_on'
        ]
        extra_kwargs = {
            'user': {'write_only': True},
            'post': {'write_only': True}
        }

    def get_likes(self, obj):
        return obj.liked.all().count()

    def get_was_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return user.is_liked(obj)
        return False

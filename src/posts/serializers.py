from rest_framework import serializers
from comments.serializers import CommentSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    likes = serializers.SerializerMethodField()
    was_liked = serializers.SerializerMethodField()    

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'username',
            'body',
            'likes',
            'was_liked',
            'created_on',
            'comments'
        ]
        extra_kwrags = {
            'user': {'write_only': True}
        }

    def __init__(self, *args, **kwargs):
        super(PostSerializer, self).__init__(*args, **kwargs)
        self.fields['comments'] = CommentSerializer(
            many=True,
            read_only=True,
            context=self.context
        )

    def get_likes(self, obj):
        return obj.liked.all().count()

    def get_was_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return user.is_liked(obj)
        return False

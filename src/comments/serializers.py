from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',            
            'username',
            'post',
            'body',
            'created_on'
        ]
        extra_kwargs = {
            'user': {'write_only': True},
            'post': {'write_only': True}
        }


    
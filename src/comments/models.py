from django.db import models
from users.models import User, Like
from posts.models import Post
from django.contrib.contenttypes.fields import GenericRelation


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    liked = GenericRelation(Like)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Comment of {} on {}>'.format(
            self.user.username,
            self.created_on
        )

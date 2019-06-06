from django.db import models
from users.models import User, Like
from django.contrib.contenttypes.fields import GenericRelation


class Post(models.Model):
    user = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    liked = GenericRelation(Like)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Post of user {} on {}>'.format(
            self.user.username,
            self.created_on
        )

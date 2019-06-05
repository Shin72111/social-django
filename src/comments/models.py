from django.db import models
from users.models import User
from posts.models import Post
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='posts',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '<Comment of {} on {}>'.format(
            self.user.username,
            self.created_on
        )
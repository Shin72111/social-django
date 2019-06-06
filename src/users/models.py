from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):
    email = models.EmailField(
        'Email Address',
        max_length=150,
        unique=True,
        error_messages={
            'unique': 'This email has been used.' +
                      ' Please register with another email'
        }
    )
    dob = models.DateField(null=True)
    about = models.TextField()
    avatar = models.ImageField(
        upload_to='images/',
        default='default_user_avatar.png'
    )
    created_on = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<User {}>'.format(self.username)

    def follow(self, user):
        if not self.is_following(user):
            self.following.create(following=user)

    def unfollow(self, user):
        if self.is_following(user):
            self.following.filter(following=user).delete()

    def is_following(self, user):
        return self == user or user.followers.filter(follower=self).count() > 0

    def like(self, obj):
        if not self.is_liked(obj):
            self.liked.create(content_type=obj)

    def unlike(self, obj):
        if self.is_liked(obj):
            self.liked.filter(content_type=obj).delete()

    def is_liked(self, obj):
        return self.liked.filter(content_type=obj).count() > 0


class Follower(models.Model):
    follower = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User,
        related_name='followers',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('follower', 'following')


class Like(models.Model):
    user = models.ForeignKey(
        User,
        related_name='liked',
        on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '<{} liked {}>'.format(self.user.username, self.content_type)

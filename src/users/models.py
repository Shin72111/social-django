from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        'Email Address',
        max_length=150,
        unique=True,
        error_messages={
            'unique': 'This email has been used. Please register with another email'
        }
    )
    dob = models.DateField(null=True)
    created_on = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    about = models.TextField()

    def __str__(self):
        return '<User {}>'.format(self.username)

    def follow(self, user):
        if self.is_following(user):
            return
        self.following.create(following=user)

    def unfollow(self, user):
        if self.is_following(user):
            self.following.filter(following=user).delete()


    def is_following(self, user):
        return self == user or self.following.filter(following=user).count() > 0

class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

    
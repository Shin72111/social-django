from django.contrib import admin
from .models import User, Follower, Like

# Register User model.
admin.site.register(User)
admin.site.register(Follower)
admin.site.register(Like)

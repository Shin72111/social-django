from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, likePost, unlikePost

router = routers.DefaultRouter()
router.register('', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:id>/like',  likePost, name='like-post'),
    path('<int:id>/unlike',  unlikePost, name='unlike-post'),
]

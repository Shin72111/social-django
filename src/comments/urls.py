from django.urls import path

from .views import likeComment, unlikeComment


urlpatterns = [
    path('<int:id>/like',  likeComment, name='like-comment'),
    path('<int:id>/unlike',  unlikeComment, name='unlike-comment'),
]

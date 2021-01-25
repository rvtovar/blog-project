from django.urls import path, include

from blog.views import PostViewSet, CommentViewSet
from rest_framework.routers import SimpleRouter

comment_detail = CommentViewSet.as_view({
    'get': "retrieve",
    'put': 'update',
    'delete': 'destroy'
})

comment_create = CommentViewSet.as_view({
    'post': 'create'
})

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')


urlpatterns = [
    # path("posts/", PostCreateApiView.as_view(), name="posts-list"),
    # path("posts/<int:pk>", PostDetailApiView.as_view(), name="post-detail"),

    # new
    path("", include(router.urls)),
    path("posts/<int:post_pk>/comment/",
         comment_create, name="post-comment"),
    path("comments/<int:pk>/", comment_detail, name="comment-detail"),
]

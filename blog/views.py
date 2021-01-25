from rest_framework import generics, viewsets, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from blog.models import Post, Comment
from blog.serializers import PostSerializer, CommentSerializer
from blog.permissions import IsAuthorOrReadOnly

# Create your views here.


# class PostCreateApiView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def perform_create(self, serializer):
#         author = self.request.user
#         serializer.save(author=author)


# class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthorOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_pk = self.kwargs.get("post_pk")
        post = get_object_or_404(Post, pk=post_pk)
        author = self.request.user
        serializer.save(post=post, author=author)


# class CommentCreateApiView(generics.CreateAPIView):
#     queryset = Comment.objects.all().order_by("id")
#     serializer_class = CommentSerializer

#     def perform_create(self, serializer):
#         post_pk = self.kwargs.get("post_pk")
#         post = get_object_or_404(Post, pk=post_pk)
#         author = self.request.user
#         serializer.save(post=post, author=author)


# class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthorOrReadOnly]

    # class PostCreateApiView(APIView):

    #     def get(self, request):
    #         posts = Post.objects.all()
    #         serializer = PostSerializer(posts, many=True)
    #         return Response(serializer.data)

    #     def post(self, request):
    #         serializer = PostSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # class PostCreateApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #     queryset = Post.objects.all()
    #     serializer_class = PostSerializer

    #     def get(self, request, *args, **kwargs):
    #         return self.list(request, *args, **kwargs)

    #     def post(self, request, *args, **kwargs):
    #         return self.create(request, *args, **kwargs)


# class PostDetailApiView(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView
# ):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class PostDetailApiView(APIView):
#     def get_object(self, pk):
#         post = get_object_or_404(Post, pk=pk)
#         return post

#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

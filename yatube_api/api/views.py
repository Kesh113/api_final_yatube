from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import (ModelViewSet, ReadOnlyModelViewSet,
                                     ViewSetMixin)

from posts.models import Post, Group, Follow
from .permissions import IsAuthor
from .serializers import (PostSerializer, GroupSerializer,
                          CommentSerializer, FollowSerializer)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = IsAuthor, IsAuthenticatedOrReadOnly
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = IsAuthenticatedOrReadOnly,


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = IsAuthor, IsAuthenticatedOrReadOnly

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(ViewSetMixin, ListCreateAPIView):
    serializer_class = FollowSerializer
    filter_backends = SearchFilter,
    search_fields = 'following__username',

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

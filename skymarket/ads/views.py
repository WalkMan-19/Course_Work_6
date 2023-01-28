from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from skymarket.ads.models import Ad, Comment
from skymarket.ads.permissions import AdOwnerPermission
from skymarket.ads.serializers import AdListSerializer, AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, \
    CommentsListSerializer, CommentCreateSerializer, CommentUpdateSerializer
from skymarket.ads.utils import AdTitleFilter


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.select_related('author').all()

    filter_backends = [DjangoFilterBackend]
    filterset_class = [AdTitleFilter]

    serializer_classes = {
        'list': AdListSerializer,
        'retrieve': AdDetailSerializer,
        'create': AdCreateSerializer,
        'partial_update': AdUpdateSerializer,
    }

    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [IsAuthenticated],
        'create': [IsAuthenticated],
        'partial_update': [AdOwnerPermission],
        'update': [AdOwnerPermission],
        'destroy': [AdOwnerPermission],
    }

    def get_permissions(self):
        return [permission() for permission in self.permission_classes_by_action[self.action]]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, AdListSerializer)

    def create(self, request, *args, **kwargs):
        request.data['author_id'] = int(self.request.user.id)
        return super().create(request, *args, **kwargs)


class AdUserOwnerListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(author_id=request.user.id)
        return super().get(request, *args, **kwargs)


class CommentPagination(pagination.PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        self.page_size = len(queryset) or self.page_size
        return super().paginate_queryset(queryset, request, view)


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    pagination_class = CommentPagination

    default_serializer_class = CommentsListSerializer
    serializer_classes = {
        'create': CommentCreateSerializer,
        'partial_update': CommentUpdateSerializer,
    }

    permission_classes_by_action = {
        'list': (IsAuthenticated,),
        'retrieve': (IsAuthenticated,),
        'create': (IsAuthenticated,),
        'partial_update': (AdOwnerPermission,),
        'update': (AdOwnerPermission,),
        'destroy': (AdOwnerPermission,),
    }

    def get_permissions(self):
        return [permission() for permission in self.permission_classes_by_action[self.action]]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return self.queryset.filter(ad_id=self.kwargs['ad_pk'])


class CommentViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        request.data['author_id'] = int(self.request.user.id)
        request.data['ad_id'] = int(self.kwargs['ad_pk'])
        return super().create(request, *args, **kwargs)

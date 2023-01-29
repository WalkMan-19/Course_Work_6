from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, CommentsViewSet, AdUserOwnerListView

ads_router = SimpleRouter()
ads_router.register('ads', AdViewSet, basename='ads')
ads_router.register(r'ads/(?P<ad_pk>[^/.]+)/comments', CommentsViewSet, basename='comments')

urlpatterns = [
    path('ads/me/', AdUserOwnerListView.as_view()),
    path('', include(ads_router.urls)),
]

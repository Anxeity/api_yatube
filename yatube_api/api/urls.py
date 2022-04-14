from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import GroupViewSet, PostViewSet, CommentViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

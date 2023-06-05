from rest_framework.routers import DefaultRouter
from posts.api.views import PostApiViwSet

router_posts = DefaultRouter()
router_posts.register(prefix='post', basename='post', viewset=PostApiViwSet)
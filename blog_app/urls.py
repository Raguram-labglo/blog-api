
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter
router = DefaultRouter()
router.register('feed', Feeds, basename='post-list')
urlpatterns = [
              path('user/', Users_list.as_view(), name='users'),
            #   path('post/', Feed.as_view(), name = 'post'),
              path('login/', LoginView.as_view(), name = 'login'),
              path('register/', Register.as_view(), name= 'register'),
              path('feed_post/',CreatePostAPIView.as_view(), name = 'feed_post'),
              path('update_post/<pk>', Feed_update.as_view(), name = 'update_post'),
              path('commants/',Commant.as_view(), name = 'commant'),
              path('feed_commants/', Commant_post.as_view()),
              #path('feed/', Feeds.as_view(), name = 'feed'),
              ]+router.urls
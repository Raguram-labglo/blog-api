
from django.urls import path, include
from .views import *

urlpatterns = [
              path('user/', Users_list.as_view(), name='users'),
              path('post/', Feed.as_view(), name = 'post'),
              path('login/', LoginView.as_view(), name = 'login'),
              path('register/', Register.as_view(), name= 'register'),
              path('feed_post/',Feed_post.as_view(), name = 'feed_post'),
              path('update_post/<pk>', Feed_update.as_view(), name = 'update_post'),
              path('commants/',Commant.as_view(), name = 'commant')
              ]
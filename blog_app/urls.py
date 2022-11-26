
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter
router = DefaultRouter()
router.register('post', CreatePostAPIView)
router.register('commant', Commant)
router.register('register', Register)
urlpatterns = [
              path('user/', Users_list.as_view()),
              path('login/', LoginView.as_view()),
              ]+router.urls
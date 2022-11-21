from .models import *
from .serializers import *


from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login

from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly


class LoginView(generics.GenericAPIView):

    serializer_class = Loginserializer

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'})
        login(request, user)
        token, li = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})


class Register(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = userSerializers


class Users_list(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = Userserializer


# class Feed(generics.ListAPIView):

#     queryset = Post.objects.all()
#     serializer_class = Posts_detail_serializer


class CreatePostAPIView(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = Posts_detail_serializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = Posts_detail_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class Feed_update(generics.RetrieveUpdateDestroyAPIView):

    #permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = Posts_detail_serializer


class Commant(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = Commant_detail_serializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class Commant_post(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Commantserializer


class Feeds(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = Feed_serializer

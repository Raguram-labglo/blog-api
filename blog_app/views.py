from .models import *
from .serializers import *


from rest_framework import generics
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login

from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

class LoginView(generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, ]
    permission_classes = [IsAuthenticated]
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

class Feed(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = Postserializer

class Feed(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = Posts_detail_erializer

class Feed_post(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = Postserializer

class Feed_update(generics.RetrieveAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = Postserializer

class Commant(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = Commantserializer
    permission_classes = [IsAuthenticatedOrReadOnly]




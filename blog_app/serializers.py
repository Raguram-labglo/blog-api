from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class Postserializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:

        model = Post
        fields = ['id','user','title', 'body', 'created']
        
class Posts_detail_serializer(serializers.ModelSerializer):
    class Meta:

        model = Post
        fields = ['id','user','title', 'body', 'created']

class userSerializers(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create_superuser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class Loginserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class Commantserializer(serializers.ModelSerializer):
    commant_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = Posts_detail_serializer()
    class Meta:
        model = Comment
        fields = ['commant_user', 'post','commant']
        

class Commant_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['commant_user', 'post', 'commant']

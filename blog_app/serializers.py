from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
#from rest_framework.fields import CurrentUserDefault

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


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
 

class Posts_detail_serializer(serializers.ModelSerializer):
    
    class Meta:
        #comment = serializers.StringRelatedField(many=True)
        model = Post
        fields = ['id','user','title', 'body', 'created']
        read_only_fields = ('user',)


class Commantserializer(serializers.ModelSerializer):
    commant_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = ['commant_user', 'post','commant']


class Commant_detail_serializer(serializers.ModelSerializer):
    post = Posts_detail_serializer()
    class Meta:
        model = Comment
        fields = [ 'post','commant_user', 'commant']


class Feed_serializer(serializers.ModelSerializer):
   # posts = Posts_detail_serializer()
    #comands = Commant_detail_serializer(source = Comment)
    class Meta:
        model = Feed
        fields = ['posts','comands']

class Home(serializers.ModelSerializer):
    commant = Commant_detail_serializer(many = True)

    class Meta:
        model = Feed
        fields = ('commant_user','post', 'commant',)

    def create(self, validated_data):

        allergies_data =validated_data.pop('allergies', [])
        names = [Post.get('') for allergy in allergies_data if allergy]
        al = Comment.objects.filter(post__id=names) # using names(list) for filtering by __in

        user1 = Feed.objects.create(**validated_data)
        user1.allergies.add(*al) 
        return user1


  
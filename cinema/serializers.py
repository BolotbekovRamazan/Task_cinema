from rest_framework import serializers

from .models import Actor, Movie

class ActorSerializer(serializers.Serializer):
   class Meta:
       model = Actor
       fields = '__all__'
class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor

        exclude = ['id']

class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie

        exclude = ['id']



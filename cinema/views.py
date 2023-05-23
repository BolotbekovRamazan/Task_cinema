# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from cinema.models import Actor, Movie
# from cinema.serializers import ActorSerializer, MovieSerializer

# @api_view(['POST'])
# def create_actor(request):
#     serializer = ActorSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

# @api_view(['GET'])
# def read_actor(request, actor_id):
#     actor = Actor.objects.get(pk=actor_id)
#     serializer = ActorSerializer(actor)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_movie(request):
#     serializer = MovieSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

# @api_view(['GET'])
# def read_movie(request, movie_id):
#     movie = Movie.objects.get(pk=movie_id)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Actor, Movie
from .serializers import ActorSerializer , MovieSerializer, ActorCreateSerializer, MovieCreateSerializer

class ActorListView(APIView):
    def get(self, request: Request):
        queryset = Actor.objects.all()
        serializer = ActorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MovieListView(APIView):
    def get(self, request: Request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ActorCreateView(APIView):
    def post(self, request: Request):
        data = request.data
        serializer = ActorCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Actor created'}, status=status.HTTP_201_CREATED)
    
class MovieCreateView(APIView):
    def post(self, request: Request):
        data = request.data
        serializer = MovieCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Movie created'}, status=status.HTTP_201_CREATED)
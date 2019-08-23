from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, viewsets, serializers
from django.contrib.auth.models import User

from api_movies.models import Movie

def ErrorResponse(text):
    return JsonResponse({'error': text})

# Serializers define the API representation.
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'imdbid']

# ViewSets define the view behavior.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer(queryset)


class Movies(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    #authentication_classes = [authentication.BaseAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(selfself, request, format=None):
        title = request.POST.get('title')
        if not title:
            return ErrorResponse('No title provided!')
        movie = Movie(title=title)
        movie.save()
        return JsonResponse({'message': 'created'})



import json
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .serializers import DisplayMoviesSerializer
from displaymovies.models import DisplayMovies
# Create your views here.


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

class DisplayMoviesDetailAPIView(mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, 
    generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes		= []
    serializer_class 			= DisplayMoviesSerializer
    queryset                    = DisplayMovies.objects.all()
    lookup_field = 'id'


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)		

class DisplayMoviesAPIView(
    mixins.CreateModelMixin, 
    generics.ListAPIView): 
    permission_classes          = []
    serializer_class            = DisplayMoviesSerializer
    passed_id                   = None
    queryset                    = DisplayMovies.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
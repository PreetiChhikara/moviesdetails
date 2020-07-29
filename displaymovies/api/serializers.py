from rest_framework import serializers

from displaymovies.models import DisplayMovies

class DisplayMoviesSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= DisplayMovies
		fields	=[
			'name',
			'popularity',
			'director',
			'genre',
			'imdb_score'
		]


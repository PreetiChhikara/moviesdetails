from django import forms

from .models import DisplayMovies

class DisplayMoviesForm(forms.ModelForm):
	class Meta:
		model 	= DisplayMovies
		fields	=[
			'name',
			'popularity',
			'director',
			'genre',
			'imdb_score'
		]

	def clean(self, *args, **kwargs):
		data = self.cleaned_data
		name = data.get('name', None)
		if name == "":
			name = None
		director = data.get("director", None)
		if director == "":
			director = None
		if name is None and director is None:
			raise forms.ValidationError('Content or image is required.')
		return super().clean(*args, **kwargs)
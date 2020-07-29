from django.db import models
from django.conf import settings

# Create your models here.


class StatusQuerySet(models.QuerySet):
	pass

class StatusManager(models.Manager):
	def get_queryset(self):
		return StatusQuerySet(self.model,using=self._db)

class DisplayMovies(models.Model):
	name		 = models.CharField(max_length=50)
	popularity	 = models.DecimalField(max_digits=3, decimal_places=1,null=True,blank=True)
	director	 = models.CharField(max_length=50)
	genre		 = models.TextField(null=True,blank=True)
	imdb_score	 = models.DecimalField(max_digits=2, decimal_places=1,null=True,blank=True)

	objects		 = StatusManager()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Movie Details'
		verbose_name_plural = 'Movies Details'
from django.db import models
from deejango.drinker.models import Drinker

class Post(models.Model):
	author = models.ForeignKey(Drinker)
	title = models.CharField(max_length=64)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	author = models.ForeignKey(Drinker)
	post = models.ForeignKey(Post)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.body

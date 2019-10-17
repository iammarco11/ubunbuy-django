from django.db import models
class search(models.Model):
	searchtext = models.SlugField(max_length=200)

	 

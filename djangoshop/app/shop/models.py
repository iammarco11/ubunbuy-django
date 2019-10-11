from django.db import models


class search(models.Model):
    searchtext = models.CharField(max_length=200)

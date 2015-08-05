from django.db import models

# Create your models here.
class Books(models.Model):    
	title = models.CharField(max_length=200)     
	author = models.CharField(max_length=100)     
	pdate = models.CharField(max_length=200)     
	pname = models.CharField(max_length=200)
	price = models.FloatField()
	sum = models.CharField(max_length=1000)
	url = models.URLField(max_length=100)
	img = models.URLField(max_length=100)

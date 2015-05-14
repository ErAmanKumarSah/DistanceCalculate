from django.db import models

# Create your models here.

class Area(models.Model):
	locality_name = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	latitude = models.CharField(max_length=30)
	longitude = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.locality_name





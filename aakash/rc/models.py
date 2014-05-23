from django.db import models

class Coordinator(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(unique=True)
	def __unicode__(self):
		return self.name
class RemoteCenter(models.Model):
	rc_id=models.IntegerField(max_length=8,unique=True)
	name=models.CharField(max_length=100)
	city=models.CharField(max_length=50)
	coordinator=models.OneToOneField(Coordinator)
	def __unicode__(self):
		return self.name

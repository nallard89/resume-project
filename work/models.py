from django.db import models

class work(models.Model):
	employer = models.CharField(max_length=200)
	position = models.CharField(max_length=200)
	start_date = models.DateField()
	end_date = models.DateField()
	job_description= models.TextField()
	


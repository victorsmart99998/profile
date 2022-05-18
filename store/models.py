from django.db import models

# Create your models here.


class Contact(models.Model):
	first_name = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	message = models.TextField(max_length=200)

	def __str__(self):
		return self.name



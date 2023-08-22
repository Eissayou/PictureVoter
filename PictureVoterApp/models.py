from django.db import models

# Create your models here.
from django.db import models

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
	
class Drawing(models.Model):
    image_data = models.TextField()  # Store the drawing data as text
    created_at = models.DateTimeField(auto_now_add=True)
    drawing_name = models.CharField(max_length=100, default="Untitled")
    rating = models.PositiveIntegerField(default=0)
    
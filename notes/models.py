from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

class Notes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150, verbose_name="Notes Title")
	body = models.TextField(max_length=500, verbose_name="Notes Body")
	last_modified = models.DateTimeField(auto_now=True)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.title}"

	def get_absolute_url(self):
		return reverse("home")
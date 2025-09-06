from django.db import models


class ProjectSubmission(models.Model):
	client_name = models.CharField(max_length=100)
	email = models.EmailField()
	project_title = models.CharField(max_length=200)
	description = models.TextField()
	submitted_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.project_title} par {self.client_name}"

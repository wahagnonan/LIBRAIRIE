from django import forms
from .models import ProjectSubmission

class ProjectSubmissionForm(forms.ModelForm):
    class Meta:
        model = ProjectSubmission
        fields = ['client_name', 'email', 'project_title', 'description']

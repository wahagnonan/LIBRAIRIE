def home(request):
	return render(request, 'base.html')
from django.shortcuts import render


from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProjectSubmissionForm

def submit_project(request):
	if request.method == 'POST':
		form = ProjectSubmissionForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'project_submitted.html')
	else:
		form = ProjectSubmissionForm()
	return render(request, 'submit_project.html', {'form': form})

from django import forms
from django.forms import ModelForm
from projects.models import Project


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "owner"]

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}), required=False)
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'owner'] # '__all__'
from django import forms
from django.forms import ModelForm

from tasks.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Добавить новую задачу ...'}))


    class Meta:
        model = Task
        fields = '__all__'

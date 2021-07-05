from django.db import models
from django.forms import fields
from .models import UserTodo
from django import forms

class UserTodoForm(forms.ModelForm):
	class Meta:
		model = UserTodo
		fields = ['title','description','important']
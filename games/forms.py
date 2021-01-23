from django.forms import ModelForm
from django import forms
from .models import Selections

class gameForm(ModelForm):
	class Meta:
		model = Selections
		fields = ['player','game','pick','ou']
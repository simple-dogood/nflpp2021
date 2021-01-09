from django.shortcuts import render
from .forms import gameForm
from .models import Selections

def home(request):

	if request.method == 'GET':
		return render(request,'games/home.html',{'form':gameForm})
	else:
		form = gameForm(request.POST)
		newForm = form.save(commit=False)
		newForm.save()

		return render(request,'games/home.html',{'form':gameForm})

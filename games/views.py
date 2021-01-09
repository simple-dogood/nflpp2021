from django.shortcuts import render
from .forms import gameForm
from .models import Selections
from django_pandas.io import read_frame

def lastPick(x):
	picks = Selections.objects.filter(player=x).order_by('created')
	lastPicks = read_frame(picks).sort_values(['game','created'],ascending=False).drop_duplicates(subset=['game'])
	return lastPicks

def home(request):

	if request.method == 'GET':
		return render(request,'games/home.html',{'form':gameForm})
	elif request.method=='POST':
		form = gameForm(request.POST)
		print(request.POST.get('player'))
		print(request.POST.get('game'))
		print(request.POST.get('pick'))
		newForm = form.save(commit=False)
		newForm.save()

		player_list = ['Bdoc']
		full_list = []
		for p in player_list:
			full_list.append(lastPick(p))

		data = Selections.objects.all()
		data.delete()

		row_flow = full_list[0].iterrows()

		objs2 = [
			Selections(
        		player = row['player'],
        		game = row['game'],
        		pick = row['pick'],
        		created = row['created'],

	    	)

	    	for index, row in row_flow
		]

		Selections.objects.bulk_create(objs2)
		picks = Selections.objects.all()

		print(full_list[0])

		
		return render(request,'games/home.html',{'form':gameForm,'picks':picks})

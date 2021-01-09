from django.db import models

class Selections(models.Model):
	player = models.CharField(max_length=50)
	game = models.CharField(max_length=50)
	pick = models.CharField(max_length=50)
	ou = models.CharField(max_length=30)
	# line = models.FloatField(default=0,blank=True)
	# total = models.FloatField(default=0,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	g_id = str(player)+"_"+str(game) 


class Standings(models.Model):
	player = models.CharField(max_length=50)
	points = models.IntegerField(default=0,blank=True)







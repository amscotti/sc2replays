from django.db import models

# Create your models here.
class Replays(models.Model):
	file = models.CharField(max_length=30)
	player1 = models.CharField(max_length=20)
	player2 = models.CharField(max_length=20)
	p1_race = models.CharField(max_length=8)
	p2_race = models.CharField(max_length=8)
	map_name = models.CharField(max_length=30)
	date_played = models.DateField()
	game_length = models.CharField(max_length=10)
	winner = models.CharField(max_length=20)
	patch_ver = models.CharField(max_length=20)
	format = models.CharField(max_length=15)
	game_category = models.CharField(max_length=20)
	
	#def __unicode__(self):
	#	return self.id
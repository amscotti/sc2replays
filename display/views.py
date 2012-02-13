# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from sc2replays.display.models import Replays
import sc2reader

def home(request):
	page_name = request.path
	if page_name == "/":
		page_name = "/home/"
	replays_list = Replays.objects.all()
	return render_to_response('replays_list.html', {'replays_list': replays_list, 'page_name': page_name})
	
def login(request):
	page_name = request.path
	return render_to_response('login.html', {'page_name': page_name})
	
def stats(request):
	page_name = request.path
	return render_to_response('replays_list.html', {'page_name': page_name})

def streams(request):
	page_name = request.path
	return render_to_response('replays_list.html', {'page_name': page_name})
	
def replay_details(request, id):
	page_name = request.path
	try:
		id = int(id)
	except ValueError:
		replays_list = Replays.objects.all()
		return render_to_response('replays_list.html', {'replays_list': replays_list, 'page_name': page_name})
	replay_query = Replays.objects.get(id=id)
	replay_file = replay_query.file
	r = sc2reader.read_file(replay_file)
	
	gametime = replay_query.game_length
	# gamedate = r.date
	gamemap = replay_query.map_name
	player1 = r.player[1].name
	player2 = r.player[2].name
	p1bneturl = r.player[1].url
	p2bneturl = r.player[2].url
	p1race = r.player[1].play_race
	p2race = r.player[2].play_race
	p1result = r.player[1].result
	p2result = r.player[2].result
	
	return render_to_response('replay_details.html', locals())
	
def replay(request):
	
	replay_query = Replays.objects.filter(id__icontains=id)
	replay_file = replay_query.id
	sc2reader_file = sc2reader.read_file(replay_file)
	gametime = r.length
	gamedate = r.date
	gamemap = r.map
	player1 = r.player[1].name
	player2 = r.player[2].name
	p1bneturl = r.player[1].url
	p2bneturl = r.player[2].url
	p1race = r.player[1].play_race
	p2race = r.player[2].play_race
	p1result = r.player[1].result
	p2result = r.player[2].result
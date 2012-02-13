# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from sc2replays.display.models import Replays

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
	
def replays(request):
	page_name = request.path
	return render_to_response('replays_list.html', {'replays_list': replays_list, 'page_name': page_name})
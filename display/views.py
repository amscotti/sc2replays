# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

def home(request):
	page_name = request.path
	if page_name == "/":
		page_name = "HOME!"
	return render_to_response('base.html', locals())
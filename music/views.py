from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'music/ngoma.html',{})

#ngoma2
def ngoma2(request):
	return render(request,'music/ngoma2.html',)

from django.shortcuts import render

from .models import work

def home(request):
	workexp = work.objects
	return render(request, 'work/home.html', {'work':workexp})
	
def resume(request):
	return render(request, 'work/resume.html')
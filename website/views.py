from django.shortcuts import render
from .models import Contact

def home(request):
	if request.method == "POST":
		#do stuff
		contact=Contact()
		email=request.POST.get('email')
		contact.email=email
		contact.save()
		return render(request, 'home.html', {})
		
	else:
		return render(request, 'home.html', {})

def robots(request):
	return render(request, 'robots.txt', {})
from django.shortcuts import render
from .models import Veterinarian
 
def indexPageView(request) :
	return render(request, 'main/index.html') 
 
def listVetsPageView(request) :
	data = veterinarians.objects.all()
	context = {"veterinarians": data}
	return render(request, "main/listvets.html", context)
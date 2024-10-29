from django.urls import path
from .views import indexPageView,listVetsPageView
from . import views 
 
urlpatterns = [
	path("", indexPageView, name="index"),   
	path("listvets", listVetsPageView, name="veterinarians"),
	path('', views.indexPageView, name='home'), 
	path('listvets/', listVetsPageView, name='veterinarians'), 
#	path("addvet/",addVeterinarianPageView,name="addvet"), 
]    

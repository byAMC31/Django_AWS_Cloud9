{"filter":false,"title":"views.py","tooltip":"/projectVet/main/views.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":2,"column":25},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":3,"column":0},"end":{"row":12,"column":57},"action":"insert","lines":["from django.shortcuts import render","from .models import Veterinarian","","def indexPageView(request):","    return render(request, 'main/index.html')","","def listVetsPageView(request):","    data = Veterinarian.objects.all()","    context = {\"veterinarians\": data}","    return render(request, \"main/listvets.html\", context)"],"id":3}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":35},"action":"remove","lines":["from django.shortcuts import render"],"id":4}],[{"start":{"row":2,"column":25},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":0,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.","from .models import Veterinarian","","def indexPageView(request):","    return render(request, 'main/index.html')","","def listVetsPageView(request):","    data = Veterinarian.objects.all()","    context = {\"veterinarians\": data}","    return render(request, \"main/listvets.html\", context)",""],"id":7},{"start":{"row":0,"column":0},"end":{"row":9,"column":54},"action":"insert","lines":["from django.shortcuts import render","from .models import Veterinarian"," ","def indexPageView(request) :","\treturn render(request, 'main/index.html') "," ","def listVetsPageView(request) :","\tdata = Veterinarian.objects.all()","\tcontext = {\"veterinarians\": data}","\treturn render(request, \"main/listvets.html\", context)"]}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["S"],"id":9}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"remove","lines":["S"],"id":10}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["s"],"id":11}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"remove","lines":["V"],"id":12},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["v"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":54},"end":{"row":9,"column":54},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1727227512662,"hash":"3663ab303fcad95dbcf6dea0572158e15fdd2c06"}
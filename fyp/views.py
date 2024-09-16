from django.shortcuts import render
from .models import Services
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home(request, page):
    services = Services.objects.all()
    paginator = Paginator(services, 3)
    services = paginator.get_page(page)
    context = {
        "services": services
    }
    return render(request, 'fyp/home.html', context)

def search(request):
	get_query = request.POST['q']
	match = Services.objects.filter(Q(services_title__icontains=get_query))
	context = {
		"services": match
	}
	return render(request, 'fyp/home.html', context)

def welcome(request):
    context = {
        "welcome": True
    }
    return render(request, 'fyp/welcome.html', context)





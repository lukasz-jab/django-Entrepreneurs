from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(request.user)
	print(args)
	print(kwargs)
	my_second_context = {
	"my_list": ['123', '456', '7890', True, '00000']
	}
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request, "home.html", my_second_context)

def contact_view(request, *args, **kwargs):
	print(request.user)
	my_context = {
		"my_text": "This is about contact info",
		"my_number": 123,
	}
	#return HttpResponse("<h1>Contact Page</h1>")
	return render(request, 'contact.html', my_context)

from django.shortcuts import render
def home_views(request):
	context = {}
	return render(request, "tumordetection/home.html", context)

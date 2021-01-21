from django.shortcuts import render
from .models import UrlTimer, Result

# Create your views here.
def index(request):
	allurls = UrlTimer.objects.all()
	results = Result.objects.all()
	temp = []
	for i in results:
		temp.append(i.url)
	return render(request, 'index.html', {'allurls': allurls,
										  'results': results,
										  'temp': temp})

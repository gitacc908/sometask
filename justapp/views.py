from django.shortcuts import render
from .models import UrlTimer, Result

from django.urls import reverse
from django.http import HttpResponseRedirect

import requests 
from bs4 import BeautifulSoup as BS



def index(request):
	allurls = UrlTimer.objects.all()
	results = Result.objects.all()
	temp = []
	for i in results:
		temp.append(i.url)
	return render(request, 'index.html', {'allurls': allurls,
										  'results': results,
										  'temp': temp})


def urlparser(request):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
	if request.method == 'POST':
		allresult = Result.objects.all()
		allurls = UrlTimer.objects.all()
		templist = []
		#collecting urls
		for i in allresult:
			templist.append(i.url)
		for urls in allurls:
			if not urls.remaining_time():
				if urls not in templist:
					resp = requests.get(urls.url, headers=headers)
					if resp.status_code == 200:
						soup = BS(resp.content, 'html.parser')
						new_result = Result(url=urls, title=str(soup.title.text), encoding=str(soup.original_encoding), h1=str(soup.find('h1')))
						new_result.save()
			
	return HttpResponseRedirect('/')


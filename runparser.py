##############################################################
#including module to django
import os, sys
from django.db import DatabaseError
import codecs

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'scraping_src.settings'

import django
django.setup()
###############################################################



from justapp.models import Result, UrlTimer, Error
import requests 
from bs4 import BeautifulSoup as BS

# making browse simulator
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

allresult = Result.objects.all()
allurls = UrlTimer.objects.all()

templist = []
# collecting urls
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
			





from django.urls import path
from .views import index, urlparser

urlpatterns = [
	path('', index, name='main'),
	path('actparsing/', urlparser, name='actparsing'),
]
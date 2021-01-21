from django.db import models
from countdowntimer_model.models import CountdownTimer
# Create your models here.

class UrlTimer(CountdownTimer):
	url = models.URLField(max_length=200, unique=True)

	def __str__(self):
		return self.url

class Result(models.Model):
    url = models.ForeignKey(UrlTimer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    encoding = models.CharField(max_length=50)
    h1 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
    	return self.title


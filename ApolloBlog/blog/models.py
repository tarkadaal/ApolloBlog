from django.db import models

class Article(models.Model):
	title = models.CharField('Title', max_length=255)
	created_date = models.DateTimeField('Publication Date')
	body = models.TextField('Body')
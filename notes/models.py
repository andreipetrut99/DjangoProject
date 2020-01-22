from django.db import models


# Create your models here.
class Notes(models.Model):
    title = models.CharField('Note title', max_length=50)
    text = models.CharField('Text', max_length=200)
    date = models.DateTimeField('Date', auto_now_add=True)

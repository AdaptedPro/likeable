import datetime

from django.db import models
from django.utils import timezone

class Image(models.Model):
    image_url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.image_url
    
    def was_uploaded_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now     

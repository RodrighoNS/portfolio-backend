from django.db import models

class Apo(models.Model):
  copyright = models.CharField(max_length=255)
  date = models.CharField(max_length=255)
  explanation = models.CharField(max_length=255)
  hdurl = models.CharField(max_length=255)
  media_type = models.CharField(max_length=255)
  service_version = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  url = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
  return self.title

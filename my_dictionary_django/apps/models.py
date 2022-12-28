from django.db import models


class english(models.Model):
  words = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
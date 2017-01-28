from __future__ import unicode_literals

from django.db import models

class ContrTask(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    # Current repeating factor
    repeat_factor = models.PositiveIntegerField(default=7)


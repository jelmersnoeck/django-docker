from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name.capitalize()

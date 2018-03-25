# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class User

class My_text(models.Model):
    """
    """
    user = models.ForeignKey(User)
    date_created = models.DateTimeField()
    text = models.CharField(max_length=400)

    def get_answers(self):
        return My_answer.objects.filter(text=self.id)

class My_answer(models.Model):
    """
    """
    user = models.ForeignKey(User)
    date_created = models.DateTimeField()
    text = models.ManyToManyField(My_text)
    answer = models.CharField(max_length=400)

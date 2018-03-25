# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import Http404

from datetime import datetime

from proj import models as md

def index(request):
    user = request.user
    context = {'user':user, }
    return render(request, 'index/index.html', context)

def select_user_type(request):
    user = request.user
    context = {'user':user, }
    return render(request, 'open_me/select_user_type.html', context)

def want_reader(request, user_id):
    user = request.user
    context = {'user':user, }

    diaries = md.User.objects.filter(is_superuser=False)
    context.update({'diaries':diaries})

    if user_id != 0:
        texts = md.My_text.objects.filter(user_id=user_id)
        context.update({'texts':texts})

    return render(request, 'open_me/want_reader.html', context)

def want_reader_save_answer(request, text_id):

    user = request.user
    context = {'user':user, }

    diaries = md.User.objects.filter(is_superuser=False)
    context.update({'diaries':diaries})

    text = md.My_text.objects.get(id=text_id)

    if request.POST:
        answer = md.My_answer()
        answer.user = md.User.objects.all()[1]
        answer.date_created = datetime.now()
        answer.save()
        answer.text.add(text)

    return render(request, 'open_me/want_reader.html', context)

def want_writer(request):
    user = request.user

    texts = md.My_text.objects.all()
    context = {'user':user,}

    if request.POST:

        print(request.POST)

        my_text = md.My_text()
        my_text.user = md.User.objects.all()[1]
        my_text.date_created = datetime.now()
        my_text.text = request.POST['InputTextArea']
        my_text.save()

    context.update({'texts':texts})

    return render(request, 'open_me/want_writer.html', context)

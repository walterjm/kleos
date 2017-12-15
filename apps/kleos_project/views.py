# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import *
import bcrypt


# Create your views here.
def index(request):
	return render(request, "kleos_project/home.html")

def get_job(request):
	return render(request, "kleos_project/get_job.html")

def submit_resume(request):
	return render(request, "kleos_project/submit_resume.html")

def employerportal(request):
	return render(request, "kleos_project/employerportal.html")

def signin(request):
	return render(request, "kleos_project/signin.html")
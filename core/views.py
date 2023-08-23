from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, "core/layout.html", {

        })


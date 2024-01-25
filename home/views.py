from django.shortcuts import render
from .models import *


def profile(request):
    context = {
        "profile": Profile.objects.first(),
        "posts": Post.objects.all(),
    }
    return render(request, "profile.html", context)

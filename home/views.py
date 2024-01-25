from django.shortcuts import render, redirect
from .models import *


def profile(request):
    context = {
        "profile": Profile.objects.first(),
        "posts": Post.objects.all(),
    }
    return render(request, "profile.html", context)


def upload(request):
    if request.method == "POST":
        picture = request.FILES.get("picture")
        Post.objects.create(picture=picture)
        return redirect("profile")
    return render(request, "upload.html")

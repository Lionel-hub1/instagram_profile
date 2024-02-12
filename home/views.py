from django.shortcuts import render, redirect
from .models import *


def profile(request):
    """The view that renders the profile page with its context."""
    context = {
        "profile" : Profile.objects.first(),
        "posts" : Post.objects.all(),
    }
    return render(request, "profile.html", context)


def upload(request):
    """The view that handles the image submission."""
    if request.method == "POST":
        image = Post()
        image.picture = request.FILES.get("picture")
        image.save()
        return redirect("profile")
    return render(request, "upload.html")

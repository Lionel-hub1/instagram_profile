from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("names", "username", "bio",
                    "profile_pic", "created_at", "updated_at")


admin.site.register(Post)

from django.contrib import admin
from .models import Profile, Video, Category, Playlist
# Register your models here.

admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(Playlist)
admin.site.register(Category)

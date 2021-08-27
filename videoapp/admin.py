from django.contrib import admin
from .models import Playlist, Uploader, Video
# Register your models here.

admin.site.register(Uploader)
admin.site.register(Video)
admin.site.register(Playlist)

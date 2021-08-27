from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth import get_user_model

User = get_user_model()


class Uploader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    # gender options? TBD
    bio = models.TextField()
    profile_picture = models.ImageField()
    channels = models.IntegerField()
    uploads = models.IntegerField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField(max_length=20)
    playlist_items = ()

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()
    views = models.IntegerField()
    uploader = models.OneToOneField(
        Uploader, on_delete=CASCADE)
    upload_date = models.DateField(auto_now_add=True)
    duration = models.DurationField()
    thumbnail = models.ImageField()
    category = models.CharField(max_length=50)
    tags = models.CharField(max_length=20)
    popular = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    # playlists = models.ManyToManyField(
    #     Playlist, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title

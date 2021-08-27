from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # gender tbd
    short_bio = models.TextField()
    profile_picture = models.ImageField()
    location = models.CharField(max_length=30)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()
    views = models.IntegerField()
    subscribers = models.IntegerField()
    uploader = models.OneToOneField(
        User, on_delete=CASCADE)
    upload_date = models.DateField(auto_now_add=True)
    duration = models.DurationField()
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    tags = models.CharField(max_length=20)
    popular = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

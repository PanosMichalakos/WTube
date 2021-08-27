from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE)
    content_object = GenericForeignKey()
    object_id = models.PositiveIntegerField()

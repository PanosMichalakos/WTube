from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=20)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE)
    content_object = GenericForeignKey()
    object_id = models.PositiveIntegerField()

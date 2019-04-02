from django.db import models
from django_unixdatetimefield import UnixDateTimeField

import uuid


class Notes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=500)
    date_create = UnixDateTimeField(auto_now_add=True)

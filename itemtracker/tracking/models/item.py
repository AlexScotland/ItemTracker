import uuid
from django.db import models


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    url = models.URLField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

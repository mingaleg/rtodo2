import uuid
from django.db import models
from django.conf import settings


class Checklist(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    title = models.CharField(
        max_length=128,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    contents = models.JSONField()

    def __str__(self):
        return f"{self.id}: {self.title}"

class Section(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    title = models.CharField(
        max_length=128,
    )
    parent = models.ForeignKey('self', null=True, blank=True, related_name='sections', on_delete=models.PROTECT)
    checklist = models.OneToOneField(Checklist, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.title}"

class Step(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    title = models.CharField(
        max_length=128,
    )
    content = models.TextField()
    section = models.ForeignKey(Section, null=True, related_name='steps', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id}: {self.title}"





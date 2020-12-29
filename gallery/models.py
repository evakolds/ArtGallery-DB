from django.db import models
from django.conf import settings
import uuid
from datetime import datetime
from django.utils import timezone


class Exhibition(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True, null=True)
    ticket_price = models.IntegerField(default=0)
    opened_at = models.DateTimeField('date opened')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    born = models.IntegerField(default=0)
    dead = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Painting(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True, null=True)
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Booking(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    tickets_number = models.IntegerField(default=1)
    booked_at = models.DateTimeField('date booked', default=timezone.now)
    code = models.CharField(max_length=200, default=uuid.uuid4, blank=True, null=True)

    def get_short_code(self):
        return str(self.code)[0:4].upper()

    def __str__(self):
        return str(self.code)

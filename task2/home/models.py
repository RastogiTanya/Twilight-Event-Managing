from django.db import models


class Everegis(models.Model):
    eventname = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=300)
    fromdate = models.DateTimeField()
    todatee = models.DateTimeField()
    deadline = models.DateTimeField()
    hostmail = models.CharField(max_length=100)
    hostPassword = models.CharField(max_length=10)

    def __str__(self):
        return self.eventname


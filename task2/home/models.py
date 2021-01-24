from django.db import models


class Everegis(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name ='ID')
    eventname = models.CharField(max_length= 100)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=300)
    fromdate = models.DateTimeField()
    todatee = models.DateTimeField()
    deadline = models.DateTimeField()
    hostmail = models.CharField(max_length=100)
    hostPassword = models.CharField(max_length=10)

    def __str__(self):
        return self.eventname

class Participants(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name= models.CharField(max_length=40)
    phone= models.CharField(max_length=14)
    email = models.CharField(max_length=70)
    eventype= models.IntegerField()
    regtype= models.CharField(max_length=20)
    people= models.IntegerField(default=1)

    def __str__(self):
        return self.name


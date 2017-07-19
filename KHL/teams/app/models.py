from django.db import models

class Team(models.Model):

    name = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)

class Player(models.Model):

    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    birthday = models.DateField(auto_now=False)
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)


class Log(models.Model):

    ip = models.GenericIPAddressField()
    url = models.URLField()
    time = models.DateTimeField()
    success = models.BooleanField()
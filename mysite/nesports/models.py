from django.db import models
from gi.overrides.Gdk import name

class Emp(models.Model):
    emp_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + " " + self.emp_id

class Nfl(models.Model):
    year = models.IntegerField()
    player = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    play = models.CharField(max_length=100)

    def __str__(self):
        return self.year + ' - ' + self.team


class NflData(models.Model):
    year = models.IntegerField()
    team = models.CharField(max_length=10)
    player = models.CharField(max_length=50)
    passyards = models.IntegerField()
    rushyards = models.IntegerField()
    touchdowns = models.IntegerField()
    two_pt = models.IntegerField()

    def __str__(self):
        return (str(self.year) + ' - ' + self.team + ' - ' + self.player)

class MlbData(models.Model):
    year = models.IntegerField()
    team = models.CharField(max_length=10)
    player = models.CharField(max_length=50)
    games = models.IntegerField()
    homeruns = models.IntegerField()
    walks = models.IntegerField()
    homeplate = models.IntegerField()

    def __str__(self):
        return (str(self.year) + ' - ' + self.team + ' - ' + self.player)


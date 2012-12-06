from django.db import models
from django.contrib.localflavor.us.models import USStateField


class Bowl(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    state = USStateField()
    slug = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Conference(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    mascot = models.CharField(max_length=100, null=True, blank=True)
    conference = models.ForeignKey(Conference, default=1)
    offense_rating = models.DecimalField("offensive rating", max_digits=5, decimal_places=3, \
                                         blank=True, null=True)
    defense_rating = models.DecimalField("defensive rating", max_digits=5, decimal_places=3, \
                                         blank=True, null=True)
    games_against_fbs = models.IntegerField("games played against FBS schools", blank=True, null=True)
    pf_against_fbs = models.IntegerField("points score against FBS schools", blank=True, null=True)
    pa_against_fbs = models.IntegerField("points allowed against FBS schools", blank=True, null=True)
    wins = models.IntegerField("overall wins", blank=True, null=True)
    losses = models.IntegerField("overall losses", blank=True, null=True)
    power_rating = models.DecimalField("power rating", max_digits=5, decimal_places=3, \
                                       blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Game(models.Model):
    SEASONS = ((u'2012', u'2012'),)

    bowl = models.ForeignKey(Bowl)
    season = models.CharField(max_length=4, choices=SEASONS)
    game_date = models.DateField()
    visitor_school = models.ForeignKey(School, related_name='visitor_school', \
                                       blank=True, null=True)
    visitor_school_score = models.IntegerField(null=True, blank=True)
    home_school = models.ForeignKey(School, related_name='home_school', \
                                    blank=True, null=True)
    home_school_score = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.season, self.bowl)

    def home_predicted_score(self):
        h = self.home_school
        v = self.visitor_school
        return int(round(((h.pf_against_fbs / float(h.games_against_fbs) - \
                float(v.defense_rating)) + \
               (v.pa_against_fbs / float(v.games_against_fbs) + \
                float(h.offense_rating))) / 2.0))

    def visitor_predicted_score(self):
        h = self.home_school
        v = self.visitor_school
        return int(round(((v.pf_against_fbs / float(v.games_against_fbs) - \
                float(h.defense_rating)) + \
               (h.pa_against_fbs / float(h.games_against_fbs) + \
                float(v.offense_rating))) / 2.0))

    class Meta:
        ordering = ('game_date', 'bowl')
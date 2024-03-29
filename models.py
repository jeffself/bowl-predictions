from django.db import models
from django.contrib.localflavor.us.models import USStateField
import math


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

    def expected_outcome(self):
        if self.visitor_school.power_rating > self.home_school.power_rating:
            high_rating = self.visitor_school.power_rating
            low_rating = self.home_school.power_rating
        else:
            high_rating = self.home_school.power_rating
            low_rating = self.visitor_school.power_rating
        return "{0:.1f}".format(( 1 / (1 + pow(10, (low_rating - high_rating) / 10))) * 100)

    def predicted_outcome(self):
        vps = self.visitor_predicted_score()
        hps = self.home_predicted_score()
        vss = self.visitor_school_score
        hss = self.home_school_score

        if vps > hps:
            if vss > hss:
                return 1
            else:
                return 0
        else:
            if hss > vss:
                return 1
            else:
                return 0

    def rankings_predicted_outcome(self):
        vranking = self.visitor_school.power_rating
        hranking = self.home_school.power_rating
        vss = self.visitor_school_score
        hss = self.home_school_score

        if vranking > hranking:
            if vss > hss:
                return 1
            else:
                return 0
        else:
            if hss > vss:
                return 1
            else:
                return 0

    def outcome_differential(self):
        vss = self.visitor_school_score
        vps = self.visitor_predicted_score()
        hss = self.home_school_score
        hps = self.home_predicted_score()

        return int(math.fabs(vss - vps) + math.fabs(hss - hps))

    def margin_differential(self):
        vss = self.visitor_school_score
        vps = self.visitor_predicted_score()
        hss = self.home_school_score
        hps = self.home_predicted_score()

        diff = (vss - hss) - (vps - hps)
        return int(math.fabs(diff))

    class Meta:
        ordering = ('game_date', 'bowl')
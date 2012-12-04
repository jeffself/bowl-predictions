from django.contrib import admin
from bowls.models import Bowl, Conference, School, Game

class BowlAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')
    prepopulated_fields = { "slug": ("name",) }
    ordering = ('name',)

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = { "slug": ("name",) }
    ordering = ('name',)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'mascot', 'conference', 'wins', 'losses', \
                    'power_rating', 'games_against_fbs', 'pf_against_fbs', \
                    'pa_against_fbs', 'offense_rating', 'defense_rating')
    ordering = ('name',)

class GameAdmin(admin.ModelAdmin):
    list_display = ('season','game_date', 'bowl', 'visitor_school', \
                    'visitor_school_predicted_score', 'visitor_school_score', \
                    'home_school', 'home_school_predicted_score', \
                    'home_school_score')
    ordering = ('game_date',)

admin.site.register(Bowl, BowlAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Game, GameAdmin)
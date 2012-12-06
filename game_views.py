from django.shortcuts import render_to_response, get_object_or_404
from bowls.models import Game

def index(request):
    game_list = Game.objects.all().order_by('game_date', 'bowl')
    return render_to_response('games/index.html', {'game_list': game_list})

def show(request, game_id):
    g = get_object_or_404(Game, pk=game_id)
    return render_to_response('games/show.html', {'game': g})

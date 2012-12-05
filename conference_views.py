from django.shortcuts import render_to_response, get_object_or_404
from bowls.models import Conference

def index(request):
    conference_list = Conference.objects.all().order_by('name')
    return render_to_response('conferences/index.html', {'conference_list': conference_list})

def show(request, conference_id):
    c = get_object_or_404(Conference, pk=conference_id)
    return render_to_response('conferences/show.html', {'conference': c})

from django.shortcuts import render_to_response, get_object_or_404
from bowls.models import Bowl

def index(request):
    bowl_list = Bowl.objects.all().order_by('name')
    return render_to_response('bowls/index.html', {'bowl_list': bowl_list})

def show(request, bowl_id):
    b = get_object_or_404(Bowl, pk=bowl_id)
    return render_to_response('bowls/show.html', {'bowl': b})

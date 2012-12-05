from django.shortcuts import render_to_response, get_object_or_404
from bowls.models import School

def index(request):
    school_list = School.objects.all().order_by('name')
    return render_to_response('schools/index.html', {'school_list': school_list})

def show(request, school_id):
    c = get_object_or_404(School, pk=school_id)
    return render_to_response('schools/show.html', {'school': c})

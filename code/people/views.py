from django.http import HttpResponse, Http404

from models import Person

def detail(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")

    return HttpResponse("Hello %s" % person.name.capitalize())

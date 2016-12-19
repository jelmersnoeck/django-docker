from django.core.management.base import BaseCommand
from people.models import Person

class Command(BaseCommand):
    help = 'Displays "Hello <name>" for the given object id'

    def add_arguments(self, parser):
        parser.add_argument('person_id', type=int)

    def handle(self, *args, **options):
        try:
            person = Person.objects.get(id=options['person_id'])
            self.stdout.write(self.style.SUCCESS('Hello ' + person.name.capitalize()))
        except Person.DoesNotExist:
            self.stdout.write(self.style.ERROR('Person not found with this id.'))

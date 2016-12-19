from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command
from django.utils.six import StringIO

from people.models import Person

def create_person(name):
    return Person.objects.create(name=name)

# Tests for the view layer.
class PersonViewTests(TestCase):
    def test_detail_view_with_invalid_id(self):
        response = self.client.get(reverse('hello-world', args=(1,)))

        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_valid_id(self):
        person = create_person("jelmer")
        response = self.client.get(reverse('hello-world', args=(person.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello Jelmer")

# Tests for the hello-world command.
class HelloWorldTest(TestCase):
    def test_hello_world_invalid_id(self):
        out = StringIO()

        call_command('hello-world', '1', stdout=out)
        self.assertIn('Person not found with this id.', out.getvalue())

    def test_hello_world_valid_id(self):
        out = StringIO()

        person = create_person("jelmer")
        call_command('hello-world', person.id, stdout=out)
        self.assertIn('Hello Jelmer', out.getvalue())

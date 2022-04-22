import factory
from faker import Factory as FakerFactory

from todo.models import TodoCategory, Todo

faker = FakerFactory.create()

class TodoCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TodoCategory

    name = factory.Faker('name')

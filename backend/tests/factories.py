import factory
from faker import Factory as FakerFactory

from todo.models import TodoCategory, Todo

faker = FakerFactory.create('ko_KR')

class TodoCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TodoCategory

    name = factory.Faker('name')

class TodoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Todo

    title = factory.Faker('name')
    category = factory.SubFactory(TodoCategoryFactory)
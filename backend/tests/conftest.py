import pytest
from todo.models import Todo, TodoCategory


@pytest.fixture(scope="session")
def category_name():
    return "This is Todo Category!"

@pytest.fixture(scope="function")
def category_in_use(db, category_name):
    return TodoCategory.objects.create(name=category_name)

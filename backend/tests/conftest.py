import pytest
from todo.models import Todo, TodoCategory
from pytest_factoryboy import register
from factories import (
    TodoCategoryFactory,
)


register(TodoCategoryFactory)

@pytest.fixture(scope="session")
def category_name():
    return "This is Todo Category!"

@pytest.fixture(scope="function")
def category_in_use(todo_category_factory, **kwargs):
    return todo_category_factory(**kwargs)

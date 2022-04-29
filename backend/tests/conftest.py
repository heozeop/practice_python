import pytest, logging
from pytest_factoryboy import register
from factories import (
    TodoCategoryFactory,
    TodoFactory,
)


register(TodoCategoryFactory)
register(TodoFactory)

@pytest.fixture(scope="function")
def category(todo_category_factory):
    return todo_category_factory()

@pytest.fixture(scope="function")
def todo(category, todo_factory):
    return todo_factory(category=category)

@pytest.fixture(scope='function')
def todo_batch(category, todo_factory):
    return todo_factory.build_batch(10, category=category)

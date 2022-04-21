import pytest

from todo.models import Todo

def test_category_create(category_in_use, category_name):
    name = category_in_use.name
    assert name is category_name

def test_todo_create(db, category_in_use):
    obj = Todo.objects.create(
        title="hello world",
        category=category_in_use,
    )
    assert obj

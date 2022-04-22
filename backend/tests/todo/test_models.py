import pytest

from todo.models import Todo

@pytest.mark.django_db
def test_todo_create(category_in_use, category_name):
    category = category_in_use
    obj = Todo.objects.create(
        title="hello world",
        category=category,
    )
    assert obj

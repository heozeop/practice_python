import pytest

from todo.models import Todo


@pytest.mark.django_db
class TestTodoModel:
    def test_todo_create(self, todo):
        obj = todo
        assert isinstance(obj, Todo)

    def test_todo_update(self, todo, category):
        title = 'new title'

        is_title_same = todo.title == title
        if is_title_same:
            todo.title = ''
            assert todo.title != title
        else:
            todo.title = title
            assert todo.title == title

        description = 'new description'
        is_desc_same = todo.content == description
        if is_desc_same:
            todo.content = ''
            assert todo.content != description
        else:
            todo.content = description
            assert todo.content == description

        todo.category = category
        assert todo.category == category


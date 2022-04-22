import pytest

@pytest.mark.django_db
class TestTodoModel:
    def test_todo_create(self, todo):
        obj = todo
        assert obj

    def test_todo_batch_create(self, todo_batch):
        is_all_category_same = True
        category_name = todo_batch[0].category.name
        for todo in todo_batch:
            if todo.category.name != category_name:
                is_all_category_same = False

        assert is_all_category_same

    def test_todo_can_create_category(self, todo_factory):
        todo = todo_factory()
        assert todo.category
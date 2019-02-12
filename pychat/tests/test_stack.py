import pytest

from pychat.utils.collections import Stack


def test_create_empty_stack():
    stack = Stack()
    assert stack.length == 0
    assert stack._Stack__array == []
    assert type(stack._Stack__array) == list


def test_create_stack_with_element():
    stack = Stack([{"name": "Anna", "age": 28}])
    assert stack.length == 1
    assert stack._Stack__array == [{"name": "Anna", "age": 28}]


def test_add_item_empty_stack():
    stack = Stack()
    stack.add({"age": 30})
    assert stack.length == 1


def test_add_item_stack_with_element():
    stack = Stack([{"age": 30}])
    assert stack.length == 1
    stack.add({"name": "Alex"})
    assert stack.length == 2


def test_remove_item_empty_stack():
    stack = Stack()
    assert stack.length == 0
    with pytest.raises(Exception):
        stack.remove()


def test_remove_item_stack_with_items():
    stack = Stack([{"age": 30, 'name': "Samuel"}, {"age": 18, 'name': "John"}])
    assert stack.length == 2
    stack.remove()
    assert stack.length == 1
    stack.remove()
    assert stack.length == 0
    with pytest.raises(Exception):
        stack.remove()


def test_get_last_item_empty_stack():
    stack = Stack()
    assert stack.length == 0
    with pytest.raises(Exception):
        stack.last_item()


def test_get_last_item_stack_with_items():
    stack = Stack([{"age": 30, 'name': "Samuel"}, {"age": 18, 'name': "John"}])
    assert stack.length == 2
    my_last_item = stack.last_item()
    assert my_last_item == {"age": 18, 'name': "John"}


def test_get_items_empty_stack():
    stack = Stack()
    assert stack.length == 0
    my_items = stack.get_items()
    assert my_items == []


def test_get_items_stack_with_items():
    stack = Stack([{"age": 19}])
    assert stack.length == 1
    my_items = stack.get_items()
    assert my_items == [{"age": 19}]


def test_clone_empty_stack():
    stack = Stack()
    new_stack = stack.clone()
    assert stack != new_stack
    assert type(stack) == Stack
    assert type(new_stack) == Stack


def test_clone_stack_with_items():
    stack = Stack([{"name": "Jessica"}])
    new_stack = stack.clone()
    assert stack != new_stack
    assert type(stack) == Stack
    assert type(new_stack) == Stack
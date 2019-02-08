import pytest

from utils.collections import Queue


def test_create_queue_empty():
    my_queue = Queue()
    assert my_queue.length == 0


def test_create_queue_with_items():
    my_queue = Queue([{"sender": "David", "receiver": "Ridwan", "message": "Hello!"}])
    assert my_queue.length == 1


def test_create_queue_with_multiple_items():
    my_queue = Queue([
        {"sender": "David", "receiver": "Ridwan", "message": "Hello!"},
        {"sender": "Ridwan", "receiver": "Ruben", "message": "Hello too!"},
        {"sender": "Ruben", "receiver": "David", "message": "Hello three!"},
    ])
    assert my_queue.length == 3


def test_enqueue():
    my_queue = Queue()
    item = {"sender": "David", "receiver": "Ridwan", "message": "Hello!"}
    assert my_queue.length == 0
    my_queue.enqueue(item)
    assert my_queue.length == 1


def test_enqueue_empty():
    my_queue = Queue()
    assert my_queue.length == 0
    with pytest.raises(Exception) as excp:
        my_queue.dequeue()


def test_dequeue():
    my_queue = Queue([{"sender": "Ridwan", "receiver": "Ruben", "message": "Hello too!"}])
    assert my_queue.length == 1
    my_queue.dequeue()


def test_dequeue_empty():
    my_queue = Queue()
    assert my_queue.length == 0


def test_fetch_items():
    my_queue = Queue([{"sender": "David", "receiver": "Ridwan", "message": "Hello!"}])
    assert my_queue.get_items() == [{"sender": "David", "receiver": "Ridwan", "message": "Hello!"}]


def test_fetch_items_empty():
    my_queue = Queue()
    assert my_queue.get_items() == []


def test_dequeue_without_items_should_throw_an_exception():
    my_queue = Queue()
    with pytest.raises(Exception) as excp:
        my_queue.dequeue()
    assert 'The queue is empty' == str(excp.value)


def test_cloning_private_array():
    my_queue = Queue()
    my_queue.enqueue({"sender": "David", "receiver": "Ridwan", "message": "Hello!"})
    my_another_queue = my_queue.clone()
    assert my_queue != my_another_queue
    assert type(my_queue) == Queue
    assert type(my_another_queue) == Queue

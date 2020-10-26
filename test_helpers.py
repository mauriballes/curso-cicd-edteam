import pytest

from peewee import *

from models import Task, create_tables
from helpers import get_all_tasks, create_task


@pytest.fixture
def context():
    db = SqliteDatabase(':memory:')
    create_tables(db)
    with db:
        db.create_tables([Task, ])

        Task.create(name='First Task')
        Task.create(name='Second Task')

        yield


def test_get_all_tasks_count(context):
    assert len(get_all_tasks()) == 2


def test_create_task(context):
    task = create_task(name='My Task')
    assert task.id == 3


def test_create_task_attributes(context):
    task = create_task(name='My Task')
    assert task.name == 'My Task'

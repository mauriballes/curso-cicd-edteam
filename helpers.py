from playhouse.shortcuts import model_to_dict
from models import Task


def get_all_tasks():
    return [model_to_dict(task) for task in Task.select()]


def create_task(name):
    return Task.create(name=name)
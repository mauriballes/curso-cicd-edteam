from peewee import *


db_proxy = Proxy()


class BaseModel(Model):
    class Meta:
        database = db_proxy


class Task(BaseModel):
    name = CharField()


def create_tables(database):
    db_proxy.initialize(database)
    with database:
        database.create_tables([Task, ])

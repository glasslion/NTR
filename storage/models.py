# -*- coding: utf-8 -*-
import datetime
import os

import peewee
from playhouse.sqlite_ext import SqliteExtDatabase



SQLITE_DB_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db.sqlite')

db = SqliteExtDatabase(SQLITE_DB_FILE)


class BaseModel(peewee.Model):
    class Meta:
        database = db

class User(BaseModel):
    username = peewee.CharField(unique=True)

class Article(BaseModel):
    id=PrimaryKeyField()
    user = peewee.ForeignKeyField(User, related_name='tweets')
    message = peewee.TextField()
    created_date = peewee.DateTimeField(default=datetime.datetime.now)
    is_published = peewee.BooleanField(default=True)

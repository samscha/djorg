from uuid import uuid4
from django.db import models


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    url = models.URLField('URL', unique=True)
    name = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    creation_date = models.DateTimeField('date created', editable=False)
    history = models.TextField(blank=True)

    # def __init__(self, name, url, creation_date):
    # self.name = name
    # self.url = url
    # self.creation_date = creation_date
    # self.history = ' ' + 'name_created:' + self.name
    # self.history = self.history + ' ' + 'url_created:' + self.url

    def __str__(self):
        return "(" + self.name + ": " + self.url + ")"

    def edit_name(self, new_name):
        self.history = self.history + ' ' + 'name_changed:' + self.name
        self.name = new_name

    def edit_url(self, new_url):
        self.history = self.history + ' ' + 'url_changed:' + self.url
        self.url = new_url

    def print_history(self):
        if (self.history == ''):
            print('No history written.')
            print('name_created: %s url_created: %s' % (self.name, self.url))

        hist = self.history.split(' ')
        for i, item in enumerate(hist):
            print("%d: %s" % (i, item))
        print('current_name: %s current_url: %s' % (self.name, self.url))

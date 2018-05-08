from uuid import uuid4
from django.db import models


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    url = models.URLField('URL', unique=True)
    name = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created = models.DateTimeField('date created', editable=False)
    history = models.TextField(blank=True)

    def __str__(self):
        return "(" + self.name + ": " + self.url + ")"

    def edit_name(self, new_name):
        if (self.history == ''):
            self.history += 'name_created: ' + self.name
            self.history += '{}url_created:' + self.url

        self.history += '{}' + 'name_changed:' + self.name
        self.name = new_name

    def edit_url(self, new_url):
        if (self.history == ''):
            self.history += 'name_created: ' + self.name
            self.history += '{}url_created: ' + self.url

        self.history += '{}' + 'url_changed: ' + self.url
        self.url = new_url

    def print_history(self):
        if (self.history == ''):
            self.history += 'name_created: ' + self.name
            self.history += '{}url_created: ' + self.url

        hist = self.history.split('{}')
        for i, item in enumerate(hist):
            print("%d: %s" % (i, item))

        print('------end')
        print('current_name: %s' % self.name)
        print('current_url: %s' % self.url)

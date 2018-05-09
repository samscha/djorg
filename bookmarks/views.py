from django.shortcuts import render

from .models import Bookmark


def index(request):
    context = {}

    context['bookmarks'] = Bookmark.objects.all()

    return render(request, 'bookmarks/index.html', context)

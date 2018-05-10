from django.shortcuts import render
from .forms import BookmarkForm
from .models import Bookmark, PersonalBookmark


def index(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        print('form', form)
        print('typeof', type(form))
        print('url', dir(form))
        if form.is_valid():
            form.save()
        else:
            print('form not valid')

    context = {}

    context['bookmarks'] = Bookmark.objects.exclude(
        id__in=PersonalBookmark.objects.values_list('id'))

    if request.user.is_anonymous:
        context['personal_bookmarks'] = PersonalBookmark.objects.none()
    else:
        context['personal_bookmarks'] = PersonalBookmark.objects.filter(
            user=request.user)

    context['form'] = BookmarkForm()

    return render(request, 'bookmarks/index.html', context)

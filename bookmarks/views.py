from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookmarkForm
from .models import Bookmark, PersonalBookmark
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
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


def delete(request, bookmark=-1):
    print('delete begin')
    print('bookmark', bookmark)

    if bookmark == -1:
        return index(request)

    context = {}

    bookmark = get_object_or_404(Bookmark, id=bookmark_id)

    if (request.method == 'POST'):
        form = BookmarkForm(request.POST, instance=bookmark)

        if form.is_valid():
            bookmark.delete()
            return HttpResponseRedirect(reverse('bookmarks:index', args=(bookmark)))
    else:
        form = BookmarkForm(instance=bookmark)

    context = {}

    # context['invalid_form'] = form

    context['bookmarks'] = Bookmark.objects.exclude(
        id__in=PersonalBookmark.objects.values_list('id'))

    if request.user.is_anonymous:
        context['personal_bookmarks'] = PersonalBookmark.objects.none()
    else:
        context['personal_bookmarks'] = PersonalBookmark.objects.filter(
            user=request.user)

    context['form'] = BookmarkForm()

    return HttpResponseRedirect('/bookmarks')

    print('delete end')
    return render(request, 'bookmarks/index.html', context)

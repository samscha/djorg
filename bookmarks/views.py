from django.shortcuts import render
from .forms import BookmarkForm
from .models import Bookmark, PersonalBookmark
from django.shortcuts import redirect, get_object_or_404


def index(request, bookmark_id=None):
    if bookmark_id:
        print('bookmark id exists')
        delete_bookmark(request, bookmark_id)

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


def delete_bookmark(request, bookmark_id):
    print('bookmark_id', bookmark_id)
    bookmark = get_object_or_404(Bookmark, id=bookmark_id)

    if (request.method == 'POST'):
        form = DeleteNewForm(request.POST, instance=bookmark)

        if form.is_valid():
            bookmark.delete()
            return HttpResponseRedirect("/bookmarks")

    else:
        form = DeleteNewForm(instance=bookmark)

    # context = {}

    # context['bookmarks'] = Bookmark.objects.exclude(
    #     id__in=PersonalBookmark.objects.values_list('id'))

    # if request.user.is_anonymous:
    #     context['personal_bookmarks'] = PersonalBookmark.objects.none()
    # else:
    #     context['personal_bookmarks'] = PersonalBookmark.objects.filter(
    #         user=request.user)

    # context['form'] = BookmarkForm()

    # return render(request, 'bookmarks/index.html', context)

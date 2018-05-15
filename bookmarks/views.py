from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import BookmarkForm
from .models import Bookmark, PersonalBookmark


@login_required
def index(request):
    if request.method == 'POST':
        if 'delete_all' in request.POST:
            if request.POST['delete_all'] == 'delete_all_confirm':
                bookmarks = Bookmark.objects.exclude(
                    id__in=PersonalBookmark.objects.values_list('id'))
                for b in bookmarks:
                    b.delete()
        elif 'id' in request.POST:
            target_id = request.POST['id']
            bookmark = Bookmark.objects.filter(pk=target_id)
            bookmark.delete()
        else:
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

    if request.method == 'POST':
        return HttpResponseRedirect(reverse('bookmarks:index'))
    return render(request, 'bookmarks/index.html', context)


# def detail(request):
#     bookmark = Bookmark.objects.all()[0]
#     # bookmark = get_object_or_404(Bookmark, id=bookmark_id)
#     return render(request, 'bookmarks/detail.html', {'bookmark': bookmark})


# def delete(request, bookmark_id):
#     print('delete begin')

#     context = {}

#     bookmark = get_object_or_404(Bookmark, id=bookmark_id)

#     if (request.method == 'POST'):
#         form = BookmarkForm(request.POST, instance=bookmark)

#         if form.is_valid():
#             bookmark.delete()
#             return HttpResponseRedirect(reverse('bookmarks:index', args=(bookmark)))
#     else:
#         form = BookmarkForm(instance=bookmark)

#     context = {}

#     # context['invalid_form'] = form

#     context['bookmarks'] = Bookmark.objects.exclude(
#         id__in=PersonalBookmark.objects.values_list('id'))

#     if request.user.is_anonymous:
#         context['personal_bookmarks'] = PersonalBookmark.objects.none()
#     else:
#         context['personal_bookmarks'] = PersonalBookmark.objects.filter(
#             user=request.user)

#     context['form'] = BookmarkForm()

#     return HttpResponseRedirect('/bookmarks')

#     print('delete end')
#     return render(request, 'bookmarks/index.html', context)

#     # <a class="EditBookmarkButtonNavLinkButton" href="{% url 'bookmarks:detail' %}">
#     #   -
#     # </a>

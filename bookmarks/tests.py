from django.db.utils import IntegrityError
from django.test import TestCase
from .models import Bookmark


class BookmarkTestCase(TestCase):
    def setUp(self):
        Bookmark.objects.create(name='This is a bookmark',
                                url='https://www.google.com')

        Bookmark.objects.create(name='This is a bookmark with a note',
                                notes='A note', url='https://www.instagram.com')

    def test_retrieving_all_bookmarks(self):
        bookmarks = Bookmark.objects.all()

        self.assertEqual(len(bookmarks), 2)

    def test_retrieving_bookmarks_by_name(self):
        bookmark = Bookmark.objects.get(name='This is a bookmark')

        self.assertEqual(bookmark.name, 'This is a bookmark')
        self.assertEqual(bookmark.notes, '')
        self.assertEqual(bookmark.url, 'https://www.google.com')

    def test_retrieving_bookmarks_by_url(self):
        bookmark = Bookmark.objects.get(url='https://www.instagram.com')

        self.assertEqual(bookmark.name, 'This is a bookmark with a note')
        self.assertEqual(bookmark.notes, 'A note')
        self.assertEqual(bookmark.url, 'https://www.instagram.com')

    def test_dupe_urls(self):
        with self.assertRaises(IntegrityError) as context:
            Bookmark.objects.create(name='This is an error bookmark',
                                    url='https://www.google.com')

        self.assertTrue(
            'UNIQUE constraint failed: bookmarks_bookmark.url' in str(context.exception))

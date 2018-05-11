from django.urls import path

from . import views

app_name = 'bookmarks'

urlpatterns = [
    path('detail/', views.detail, name='detail'),
    path('', views.index, name='index'),
]

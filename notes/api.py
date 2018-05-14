from django.conf import settings
from rest_framework import serializers, viewsets
from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to define the API representation for Notes."""

    class Meta:
        model = Note
        fields = ('title', 'content')

    def create(self, validated_data):
        """Override create to associate current user with new note."""
        user = self.context['request'].user
        note = Note.objects.create(user=user, **validated_data)
        return note


class NoteViewSet(viewsets.ModelViewSet):
    """Viewset to define the view behavior for Notes"""

    serializer_class = NoteSerializer
    # queryset = Note.objects.all()
    queryset = Note.objects.none()
    # queryset = Note.objects.filter(api_enabled=True)

    def get_queryset(self):
        user = self.request.user
        if settings.DEBUG == True:
            return Note.objects.all()
        elif user.is_anonymous:
            return Note.objects.none()
        else:
            return Note.objects.filter(user=user)

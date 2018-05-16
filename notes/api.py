from django.conf import settings
from rest_framework import serializers, viewsets
from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to define the API representation for Notes."""

    class Meta:
        model = Note
        fields = ('title', 'content', 'id')

    def create(self, validated_data):
        """Override create to associate current user with new note."""
        user = self.context['request'].user
        note = Note.objects.create(user=user, **validated_data)
        return note

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    # def delete(self, request, pk, format=None):
    #     note = self.get_object(pk)
    #     note.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


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

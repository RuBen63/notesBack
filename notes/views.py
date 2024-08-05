from rest_framework import viewsets
from .models import Notes
from .serializer import NotesSerializer


# Create your views here.
class NotesView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
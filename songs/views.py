from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from rest_framework import generics
from albums.models import Album
from django.shortcuts import get_object_or_404


class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.filter(album=self.kwargs.get("pk"))

    def perform_create(self, serializer) -> None:
        album = get_object_or_404(Album, id=self.kwargs.get("pk"))
        serializer.save(album=album)

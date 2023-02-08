from rest_framework import generics
from .models import Work, Artist
from .serializers import WorkSerializer, ArtistSerializer

class WorkList(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    def get_queryset(self):
        queryset = self.queryset
        work_type = self.request.query_params.get('work_type', None)
        artist = self.request.query_params.get('artist', None)
        if work_type is not None:
            queryset = queryset.filter(work_type=work_type)
        if artist is not None:
            queryset = queryset.filter(artist__name=artist)
        return queryset

class UserRegistration(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer

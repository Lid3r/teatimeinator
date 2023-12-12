from rest_framework import viewsets
from .serializers import userSerializers
from user.models import Fren


class userviewsets(viewsets.ModelViewSet):
    queryset = Fren.objects.all()
    serializer_class = userSerializers

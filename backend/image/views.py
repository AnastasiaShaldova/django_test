from rest_framework import mixins, viewsets
from rest_framework.parsers import MultiPartParser

from .models import ImagesModel
from .serializers import ImageSerializer, ImageCreateSerializer


class ImagesAllViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return ImagesModel.objects.all()


class ImagesCreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ImageCreateSerializer
    parser_classes = [MultiPartParser]


class ImagesDeleteViewSet(viewsets.GenericViewSet, mixins.DestroyModelMixin):
    queryset = ImagesModel.objects.all()
    serializer_class = ImageSerializer

from rest_framework import mixins, viewsets

from .models import ImagesModel
from .serializers import ImageSerializer


class ImagesAllViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return ImagesModel.objects.all()


class ImagesCreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ImageSerializer


class ImagesDeleteViewSet(viewsets.GenericViewSet, mixins.DestroyModelMixin):
    queryset = ImagesModel.objects.all()
    serializer_class = ImageSerializer

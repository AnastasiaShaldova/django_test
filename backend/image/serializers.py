from rest_framework import serializers

from .models import ImagesModel


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImagesModel
        fields = '__all__'

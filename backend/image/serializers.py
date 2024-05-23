import base64

from rest_framework import serializers

from .models import ImagesModel


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImagesModel
        fields = '__all__'


class ImageCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = ImagesModel
        fields = '__all__'

    def create(self, validated_data):
        image_file = validated_data.pop('image')
        image_base64 = self.convert_image_to_base64(image_file)
        validated_data['image'] = image_base64
        return super().create(validated_data)

    def convert_image_to_base64(self, image_file):
        image_data = image_file.read()
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        return image_base64

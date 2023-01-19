from rest_framework import serializers
from rest_framework.utils import model_meta

from app import models


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Status
        fields = ('url', 'id', 'description')
        read_only_fields = ('url', 'id',)


class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Color
        fields = ('url', 'id', 'color')
        read_only_fields = ('url', 'id',)


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    color = ColorSerializer()
    status = StatusSerializer()

    class Meta:
        model = models.Item
        fields = ('url', 'id', 'description', 'brand', 'color', 'status')
        read_only_fields = ('url', 'id',)

    def create(self, validated_data):
        status_data = validated_data.pop('status')
        status, _ = models.Status.objects.get_or_create(**status_data)
        color_data = validated_data.pop('color')
        color, _ = models.Color.objects.get_or_create(**color_data)
        order = models.Item.objects.create(**validated_data, status=status, color=color)
        return order

    def update(self, instance, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations:
                value, _ = info.relations[attr].related_model.objects.get_or_create(**value)
            setattr(instance, attr, value)
        instance.save()
        return instance

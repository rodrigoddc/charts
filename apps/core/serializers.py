from rest_framework import serializers

from apps.core.models import DataSample


class DataSampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataSample
        fields = [
            'month',
            'price'
        ]

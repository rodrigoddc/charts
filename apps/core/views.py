import json

from django.core import serializers
from django.http import JsonResponse, Http404
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataSample
from .serializers import DataSampleSerializer


class IndexView(TemplateView):
    template_name = 'core/index.html'


class DataJsonViewSet(APIView):

    def get(self, request, format=None):

        data = DataSample.objects.all()
        serializer = DataSampleSerializer(data, many=True)

        return Response(serializer.data)



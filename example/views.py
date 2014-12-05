from rest_framework import generics
from example import models
from example import serializers


class ExampleList(generics.ListAPIView):
    queryset = models.Example.objects.all()
    serializer_class = serializers.ExampleSerializer


class ExampleDetail(generics.RetrieveAPIView):
    queryset = models.Example.objects.all()
    serializer_class = serializers.ExampleSerializer

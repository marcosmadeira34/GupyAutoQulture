from rest_framework import serializers
from . import models 


class ResultsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ResultsModel 
        fields = '__all__'
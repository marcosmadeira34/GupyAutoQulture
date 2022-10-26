from rest_framework import serializers
from . models import ResultModel, CandidateModel, JobModel 


class ResultsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResultModel 
        fields = '__all__'


class CandidateHiredSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CandidateModel 
        fields = '__all__'
from graphene_django import DjangoObjectType
from . models import ResultModel, CandidateModel, JobModel, ManualCandidateModel, ScoreModel


class ResultsModelType(DjangoObjectType):
    class Meta:
        model = ResultModel
        fields = "__all__"

class CandidateModelType(DjangoObjectType):
    class Meta:
        model = CandidateModel
        fields = "__all__"

class JobModelType(DjangoObjectType):
    class Meta:
        model = JobModel
        fields = "__all__"

class ManualCandidateModelType(DjangoObjectType):
    class Meta:
        model = ManualCandidateModel
        fields = "__all__"

class ScoreModelType(DjangoObjectType):
    class Meta:
        model = ScoreModel
        fields = "__all__"
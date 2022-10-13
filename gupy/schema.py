import graphene
from graphene_django import DjangoObjectType
from gupy.models import ResultsModel, CandidateModel, JobModel, ManualCandidateModel, ScoreModel


class ResultsModelType(DjangoObjectType):
    class Meta:
        model = ResultsModel
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


class Query(graphene.ObjectType):
    all_results = graphene.List(ResultsModelType)
    all_candidates = graphene.List(CandidateModelType)
    all_jobs = graphene.List(JobModelType)
    all_manual_candidates = graphene.List(ManualCandidateModelType)
    all_scores = graphene.List(ScoreModelType)

    def resolve_all_results(self, info, **kwargs):
        return ResultsModel.objects.select_related('candidate').all()

    def resolve_all_candidates(self, info, **kwargs):
        return CandidateModel.objects.select_related('result').all()

    def resolve_all_jobs(self, info, **kwargs):
        return JobModel.objects.select_related('name').all()
    
    def resolve_all_manual_candidates(self, info, **kwargs):
        return ManualCandidateModel.objects.select_related('job').all()

    def resolve_all_scores(self, info, **kwargs):
        return ScoreModel.objects.select_related('score').all()


schema = graphene.Schema(query=Query)
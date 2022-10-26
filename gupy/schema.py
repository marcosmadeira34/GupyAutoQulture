import graphene
import requests  
from .types import ResultsModelType, CandidateModelType, JobModelType, ManualCandidateModelType, ScoreModelType
from .models import ResultModel, CandidateModel, JobModel, ManualCandidateModel, ScoreModel
from .mutations import CreateCandidateHiredMutation


class Query(graphene.ObjectType):
    all_results = graphene.List(ResultsModelType)
    all_candidates = graphene.List(CandidateModelType)
    all_jobs = graphene.List(JobModelType)
    all_manual_candidates = graphene.List(ManualCandidateModelType)
    all_scores = graphene.List(ScoreModelType)

    def resolve_all_results(self, info, **kwargs):
        return ResultModel.objects.all()

    def resolve_all_candidates(self, info, **kwargs):
        return CandidateModel.objects.all()

    def resolve_all_jobs(self, info, **kwargs):
        return JobModel.objects.all()
    
    def resolve_all_manual_candidates(self, info, **kwargs):
        return ManualCandidateModel.objects.all()

    def resolve_all_scores(self, info, **kwargs):
        return ScoreModel.objects.all()


class Mutation(graphene.ObjectType):
    candidate_hired = graphene.Field(CreateCandidateHiredMutation)



schema = graphene.Schema(query=Query, mutation=Mutation)
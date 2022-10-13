from django.contrib import admin
from gupy.models import ResultsModel, CandidateModel, JobModel, ManualCandidateModel, ScoreModel

# Register your models here.
admin.site.register(ResultsModel)
admin.site.register(CandidateModel)
admin.site.register(JobModel)
admin.site.register(ManualCandidateModel)
admin.site.register(ScoreModel)

from django.contrib import admin
from gupy.models import ResultModel, CandidateModel, JobModel

# Register your models here.
admin.site.register(ResultModel)
admin.site.register(CandidateModel)
admin.site.register(JobModel)



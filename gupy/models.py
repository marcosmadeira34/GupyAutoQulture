from django.db import models

# Create your models here.
class ResultsModel(models.Model):
    result_id = models.IntegerField()
    partnerName = models.CharField(max_length=100)
    endedAt = models.DateTimeField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    tags = models.CharField(max_length=100)


class CandidateModel(models.Model):
    result = models.ForeignKey(ResultsModel, on_delete=models.CASCADE)
    birthdate = models.DateField()
    candidate_id = models.IntegerField()
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    identificationDocument = models.CharField(max_length=255)
    countryOfOrigin = models.CharField(max_length=255)
    linkedinProfileUrl = models.URLField()
    gender = models.CharField(max_length=255)
    mobileNumber = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)

class JobModel(models.Model):
    candidate = models.ForeignKey(CandidateModel, on_delete=models.CASCADE)
    job_id = models.IntegerField()
    name = models.CharField(max_length=255)

class ManualCandidateModel(models.Model):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    manualCandidate_id = models.IntegerField()
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

class ScoreModel(models.Model):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    score = models.IntegerField()

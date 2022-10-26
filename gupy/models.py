from django.db import models

# Create your models here.
 
class ResultModel(models.Model):    
    partnerName = models.CharField(max_length=100)
    job_Id = models.CharField(max_length=100, default=None, null=True, blank=True)
    job_Name = models.CharField(max_length=100, default=None, null=True, blank=True)
    candidate_Id = models.CharField(max_length=100, default=None, null=True, blank=True)
    score = models.CharField(max_length=100, default=None, null=True, blank=True)
    name = models.CharField(max_length=100, default=None, null=True, blank=True)
    lastName = models.CharField(max_length=100, default=None, null=True, blank=True)
    gender = models.CharField(max_length=100, default=None, null=True, blank=True)
    email = models.CharField(max_length=100, default=None, null=True, blank=True)
    mobileNumber = models.CharField(max_length=100, default=None, null=True, blank=True)
    phoneNumber = models.CharField(max_length=100, default=None, null=True, blank=True)
    candidate_birthdate = models.CharField(max_length=100, default=None, null=True, blank=True)
    identificationDocument = models.CharField(max_length=100, default=None, null=True, blank=True)
    countryOfOrigin = models.CharField(max_length=100, default=None, null=True, blank=True)
    currentStepId = models.CharField(max_length=100, default=None, null=True, blank=True)
    currentStepName = models.CharField(max_length=100, default=None, null=True, blank=True)
    currentStepStatus = models.CharField(max_length=100, default=None, null=True, blank=True)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    endedAt = models.DateTimeField()
    linkedinProfileUrl = models.CharField(max_length=100, default=None, null=True, blank=True)
    manualCandidate = models.CharField(max_length=100, null=True, default=None, blank=True)
    result_id = models.CharField(max_length=100, default=None, null=True, blank=True)
    tags = models.CharField(max_length=100)

    


class CandidateModel(models.Model):
    
    birthdate = models.DateField()
    candidate = models.IntegerField()
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    identificationDocument = models.CharField(max_length=255)
    countryOfOrigin = models.CharField(max_length=255)
    linkedinProfileUrl = models.URLField()
    gender = models.CharField(max_length=255)
    mobileNumber = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255, default=None, null=True)
    creaedAt = models.DateTimeField(default=None)
    
    



class JobModel(models.Model):
    candidate = models.ForeignKey('CandidateModel', on_delete=models.CASCADE)
    job_id = models.IntegerField()
    name = models.CharField(max_length=255)

class ManualCandidateModel(models.Model):
    job = models.ForeignKey('JobModel', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

class ScoreModel(models.Model):
    job = models.ForeignKey('JobModel', on_delete=models.CASCADE)
    score = models.IntegerField()

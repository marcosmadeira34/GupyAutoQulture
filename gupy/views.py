from django.shortcuts import render
from . import serializers
from rest_framework import viewsets
from . import models 

class ResultsViews(viewsets.ModelViewSet):
    queryset = models.ResultsModel.objects.all()
    serializer_class = serializers.ResultsSerializer
# Create your views here.

    def get_listings_application(request):
        api = GupyApi()
        response = api.listing_application()

        if len(response['results']) > 1:
            for application in response['results']:
                default = dict(
                        id = application['id'],
                        partnerName = application['partnerName'],                         
                        endedAt = application['endedAt'],
                        createAt = application['createAt'],
                        updatedAt = application['updatedAt'],
                        tags = application['tags'],
                        birthdate = application['candidate']['birthdate'],
                        idCandidate = application['candidate']['id'],
                        name = application['candidate']['name'],
                        lastName = application['candidate']['lastName'],
                        email = application['candidate']['email'],
                        identificationDocument = application['candidate']['identificationDocument'],
                        countryOfOrigin = application['candidate']['countryOfOrigin'],                                          
                        linkedinProfileUrl = application['candidate']['linkedinProfileUrl'],
                        gender = application['candidate']['gender'],
                        mobileNumber = application['candidate']['mobileNumber'],
                        phoneNumber = application['candidate']['phoneNumber'], 

                        idJob = application['job']['id'],
                        nameJob = application['job']['name'],

                        manualCandidate = application['manualCandidate'],

                        currentStepId = application['currentStep']['id'],
                        currentStepName = application['currentStep']['name'],
                        currentStepStatus = application['currentStep']['status'],

                        score = application['score']
                )                          
                obj, created = models.ResultsModel.objects.update_or_create(defaults=default, id=application['id'])

                if len(response['results']) < 1:
                    break
        




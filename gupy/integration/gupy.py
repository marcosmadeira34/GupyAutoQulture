from typing import Union
import os
import requests
from requests import Response
import requests_cache
from urllib.parse import urljoin
from credentials import GUPY_TOKEN, GUPY_API_URL_BASE, CACHE_TTL

from urllib.parse import urljoin
from . models import ResultsModel


requests_cache.install_cache(
            'gupy_cache',
            backend='sqlite', 
            expire_after=CACHE_TTL
        )

class GupyApi:
    def __init__(self):
        self.token = 'a0b69daf-8086-4e8f-8fca-dd473c220e8b'
        self.base_url = GUPY_API_URL_BASE

    def listing_application(self):
        """Retorna todas as aplicações de candidatos que foram 
        contratados para o cargo na empresa"""
        jobId = [
                '3045933', '3070825', '3051608', '3051703',
                '3061852', '3120953', '3108344', '3072878'
                ]
        for job in jobId:
            offset = 1
            while True:
                url = f'https://api.gupy.io/api/v1/jobs/{job}/applications?status=hired&order=id%20asc&perPage=100&page={offset}'
                headers = {
                    'accept': 'application/json',
                    'authorization': f'Bearer {self.token}'  
                    }
                request = requests.get(url, headers=headers)
                response = request.json()
                offset += 1
                #print(response)

                """ if len(response['results']) > 1:
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
 """
""" if __name__ == '__main__':
    gupy = GupyApi()
    gupy.listing_application()
 """



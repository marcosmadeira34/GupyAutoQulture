from gupy.models import ResultModel
from gupy.gupy import GupyApi
from gupy.serializers import ResultsSerializer
from rest_framework import viewsets
from gupy.credentials import GUPY_TOKEN, GUPY_API_URL_BASE, CACHE_TTL
import requests
import json


class ResultsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ResultModel.objects.all().order_by('-updatedAt')
    serializer_class = ResultsSerializer

class GupyApi(viewsets.ModelViewSet):
    def __init__(self):
        self.token_gupy = ''
        self.token_qr = ''
        self.base_url_qr = 'https://app.qulture.rocks'
# Create your views here.

    def get_listings_application(self):
        jobId = [
                                 
                ]

        for job in jobId:
            offset = 1
            while True:
                
                url = f'https://api.gupy.io/api/v1/jobs/{job}/applications?status=hired&order=id%20asc&perPage=100&page={offset}'               
                headers_gupy = {
                    'accept': 'application/json',
                    'authorization': f'Bearer {self.token_gupy}'  
                    }
                request = requests.get(url=url, headers=headers_gupy)
                response = request.json()                
                print(response)
            
                if len(response['results']) > 1:
                    for application in response['results']:
                        default = dict(
                                id = application['id'],
                                name = application['candidate']['name'],
                                lastName = application['candidate']['lastName'],
                                email = application['candidate']['email'],
                                gender = application['candidate']['gender'],
                                mobileNumber = application['candidate']['mobileNumber'],
                                phoneNumber = application['candidate']['phoneNumber'], 
                                job_Id = application['job']['id'],
                                job_Name = application['job']['name'],
                                identificationDocument = application['candidate']['identificationDocument'],
                                candidate_birthdate = application['candidate']['birthdate'],
                                countryOfOrigin = application['candidate']['countryOfOrigin'],                                          
                                linkedinProfileUrl = application['candidate']['linkedinProfileUrl'],
                                currentStepId = application['currentStep']['id'],
                                currentStepName = application['currentStep']['name'],
                                currentStepStatus = application['currentStep']['status'],
                                partnerName = application['partnerName'],                         
                                endedAt = application['endedAt'],
                                createdAt = application['createdAt'],
                                updatedAt = application['updatedAt'],
                                tags = application['tags'],
                                candidate_Id = application['candidate']['id'],
                                manualCandidate = application['manualCandidate'],
                                score = application['score']
                        )                          
                        
                        created = ResultModel.objects.update_or_create(defaults=default, id=application['id'])
                        #print(obj, created)
                        offset += 1                 

                if len(response['results']) < 1:
                    break

    
    def post_user_imports_qr(self):    
        
        url_qr = f'{self.base_url_qr}/api_integration/user_importers'
        headers_qr = {
                    'Accept': 'application/json',
                    'Authorization': f'Bearer {self.token_qr}'
                }
        created = ResultModel.objects.all()

        for user in created:

            payload_qr = {  
                            "user_importer": {
                            "data": [{
                                "name": str(user.name),
                                "active": 1,
                                "email": str(user.email),
                                "cpf": str(user.identificationDocument),
                                "country": str(user.countryOfOrigin),                            
                                "job_title": str(user.job_Name),
                                "gender": "rather_not_answer",                            
                                "admission_date": str(user.endedAt),
                                "last_career_move_date": "2016-01-30"
                                },
                        {
                            "name": user.name,
                            "active": True,
                            "email": user.email,
                            "tags": ["consultor", "gerente"]
                                }
                                ]
                            }
                        }

            request_qr = requests.post(url=url_qr, headers=headers_qr, json=payload_qr)
            print(request_qr.status_code)
            print(request_qr.reason)
            result = request_qr.json()
            print(result)
        
            #offset += 1

app = GupyApi()
app.get_listings_application()
app.post_user_imports_qr()

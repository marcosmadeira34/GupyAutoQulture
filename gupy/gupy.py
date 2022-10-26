import os
import requests
from requests import Response
import requests_cache
from urllib.parse import urljoin
from gupy.integration.credentials import GUPY_TOKEN, GUPY_API_URL_BASE, CACHE_TTL

from urllib.parse import urljoin




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
                request = requests.get(url=url, headers=headers)
                response = request.json()
                offset += 1
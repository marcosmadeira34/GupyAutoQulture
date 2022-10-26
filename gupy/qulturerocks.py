import requests 
import json 
import os 
import requests_cache

requests_cache.install_cache(
            'gupy_cache',
            backend='sqlite', 
            expire_after=CACHE_TTL
        )

class QultureRocks:
    def __init__(self):
        self.token_qr = "bc978c6c926a39c4b38df4f18b19e49a3b5c5507c4e30616d990f81de3f801b7"
        self.base_url_qr = 'api.qulture.rocks'

        def user_import_create(self):
            url = f'{self.base_url}/api_integration/user_importers'
            
            headers = {
                'accept': 'application/json',
                'authorization': f'Bearer {self.token}'
            }
            payload = {
                        "user_importer": {
                            "send_invite_mails": true,
                            "data": [
                            {
                                "name": "joao",
                                "active": true,
                                "email": "joao@example.com.br",
                                "tags": ["consultor"],
                                "supervisor_email": "davi@example.com.br",
                                "supervisor_cpf": "30312345689",
                                "area": "North",
                                "location": "Westeros",
                                "level": "Reborn",
                                "rg": "123456789",
                                "cpf": "43000086390",
                                "country": "Westeros",
                                "education": "N/A",
                                "department": "Ice",
                                "job_title": "King in the North",
                                "nickname": "Knows nothing",
                                "sex": "male",
                                "gender": "cis_man",
                                "remove_supervisor": false,
                                "termination_reason": null,
                                "birth_date": "1990-01-30",
                                "termination_date": null,
                                "admission_date": "2015-11-01",
                                "last_career_move_date": "2016-01-30"
                            },
                            {
                                "name": "davi",
                                "active": true,
                                "email": "davi@example.com.br",
                                "tags": ["consultor", "gerente"]
                            }
                            ]
                        }
}
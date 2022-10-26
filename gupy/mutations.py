import graphene
from .types import ResultsModelType, CandidateModelType, JobModelType, ManualCandidateModelType, ScoreModelType
from .models import ResultModel, CandidateModel, JobModel, ManualCandidateModel, ScoreModel
from graphene_django.rest_framework.mutation import SerializerMutation
from .serializers import CandidateHiredSerializer
import json

class CreateCandidateHiredSerializerMutation(SerializerMutation):
    class Meta:
        serializer_class = CandidateHiredSerializer


class CreateCandidateHiredMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        candidate_id = graphene.Int()
        name = graphene.String()
        lastName = graphene.String()
        email = graphene.String()
        identificationDocument = graphene.String()
        countryOfOrigin = graphene.String()
        linkedinProfileUrl = graphene.String()
        gender = graphene.String()
        mobileNumber = graphene.String()
        phoneNumber = graphene.String()
        birthdate = graphene.Date()

    candidate = graphene.Field(CandidateModelType)

    def mutate(self, info, id, candidate_id, name, lastName, email, 
                identificationDocument, countryOfOrigin, linkedinProfileUrl,
                gender, mobileNumber, phoneNumber, birthdate):
        
        candidate = CandidateModel.objects.create(
            id=id,
            candidate_id=candidate_id,
            name=name,
            lastName=lastName,
            email=email,
            identificationDocument=identificationDocument,
            countryOfOrigin=countryOfOrigin,
            linkedinProfileUrl=linkedinProfileUrl,
            gender=gender,
            mobileNumber=mobileNumber,
            phoneNumber=phoneNumber,
            birthdate=birthdate)  

        candidate.save()
        url = 'api.qulture.rocks/graphql/3895'
        payload = {
            "query": "mutation { candidateHired(id: 1, candidate_id: 1, name: \"Teste\", lastName: \"Teste\", email: \)}"
        }
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer bc978c6c926a39c4b38df4f18b19e49a3b5c5507c4e30616d990f81de3f801b7'}
        request = requests.post(url=url, data=payload, headers=headers)
        response = request.json()
        print(response)


        return CreateCandidateHiredMutation(candidate_hired=candidate)
            

from django.urls import path, include, re_path
from . import views
from rest_framework import routers
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()
router.register(r'api', views.ResultsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
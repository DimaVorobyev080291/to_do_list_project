from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from to_do_list_app.models import To_do_list
from to_do_list_app.serializers import To_do_listSerializer


class To_do_list_ViewSet(ModelViewSet):
    queryset = To_do_list.objects.all()
    serializer_class = To_do_listSerializer
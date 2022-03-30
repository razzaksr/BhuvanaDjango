from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Corporates

class CorpSeri(ModelSerializer):
    class Meta:
        model=Corporates
        fields=('org','ratings','opennings','basic','nature','employees','place')

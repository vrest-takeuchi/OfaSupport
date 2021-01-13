

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from app1_output.models import AnaSummary


def app1(request):

    df=AnaSummary.objects.all()

    post_list = serializers.serialize('json', df)
    return HttpResponse(post_list)
# Create your views here.

# Create your views here.

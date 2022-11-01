from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
# Create your views here.


def index(request):
    responseData = {
        'slackUsername': 'basilokache',
        'backend': True,
        'age': 27,
        'bio': 'I am a software engineer'

    }

    return JsonResponse(responseData)
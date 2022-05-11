from django.http import HttpResponse
from django.shortcuts import render

from .models import Course

def main(request):
    return HttpResponse(
        '<h1><u>Main</u></h1>'
    )

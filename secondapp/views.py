from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return HttpResponse(
        '<h1><u>Main</u></h1>'
    )

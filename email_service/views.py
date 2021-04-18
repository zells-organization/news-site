from django.shortcuts import render
from django.http.response import HttpResponse
from .tasks import sample_task


# Create your views here.

def mail_test(request):
    print('before')
    result = sample_task.delay()
    print('after')
    return HttpResponse(f'{result.id}')

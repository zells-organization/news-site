from django.shortcuts import render
from django.http.response import HttpResponse
from .tasks import sample_task


# Create your views here.

def mail_test(request):
    result = sample_task.delay()
    return HttpResponse(f'{result.task_id}')

from django.urls import path

from .views import *

urlpatterns = [
    path('hello/', StartView.as_view(), name='start'),
]

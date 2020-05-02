from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='start'),
    path('', MainView.as_view(), name='main'),
]

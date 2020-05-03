from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', MainView.as_view(), name='main'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

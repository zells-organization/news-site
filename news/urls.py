from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', MainView.as_view(), name='main'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('premoderation/', PremoderationView.as_view(), name='premoderation'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('posts/', CreatePostView.as_view(), name='create-post')
]

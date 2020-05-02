from django.contrib.auth.backends import ModelBackend
from news.models import User
from django.core.exceptions import ValidationError

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            raise ValidationError(f"{username} does not exist")
        else:
            if user.check_password(password):
                return user
        raise ValidationError("Incorrect password")

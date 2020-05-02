from django.db import models
from .base_model import BaseModel
from .user import User

class Post(BaseModel):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField()
    is_approved = models.BooleanField(default=False)
    
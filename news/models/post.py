from django.db import models
from .base_model import BaseModel
from .user import User


class Post(BaseModel):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    text = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author} - {self.title}"

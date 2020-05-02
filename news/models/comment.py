from django.db import models
from .base_model import BaseModel
from .post import Post
from .user import User


class Comment(BaseModel):
    to_post = models.ForeignKey(Post, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField()

from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
        owner = models.ForeignKey(User)
        title = models.TextField()
        static_content = models.TextField()

class Post(models.Model):
        author = models.ForeignKey(User)
        content = models.TextField()
        title = models.TextField()
        related_to = models.ForeignKey(Blog)
        
class Comment(Post):
        refers_to = models.ForeignKey(Post)
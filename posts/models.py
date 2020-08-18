from django.db import models

class PostsModel(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text

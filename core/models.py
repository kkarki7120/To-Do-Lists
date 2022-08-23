
from django.db import models
from django.contrib.auth.models import User



class List(models.Model):
    title = models.CharField(max_length=100, blank=False )
    description = models.CharField(max_length = 400, null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    

    

# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Pin(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pins/')
    board = models.ForeignKey(Board, related_name='pins', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Pin(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pins/')
    board = models.ForeignKey(Board, related_name='pins', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # Make this field nullable

    def __str__(self):
        return self.title
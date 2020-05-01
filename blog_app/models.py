from django.db import models
from django.urls import reverse

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
   
    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])
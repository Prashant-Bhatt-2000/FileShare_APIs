from django.db import models
from accounts.models import User

# Create your models here.
class Files(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
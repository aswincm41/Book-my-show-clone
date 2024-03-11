from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    year = models.DateField(null=True)
    image=models.ImageField(upload_to='pics')
    background_image=models.ImageField(upload_to='bg',null=True,blank=True)

    def __str__(self):
        return self.name

    
# Create your models here.













from django.db import models

# Create your models here.
#this is a normal class this is support create a orm model for that we need a class which support model
"""class Destination:
    id: int
    name:str
    disc:str
    img:str
    price:int
    offer:bool """

# django supports to specific   type of column
class Destination(models.Model):
    Name=models.CharField(max_length=50)
    Disc=models.TextField()
    Price=models.IntegerField()
    Img=models.ImageField(upload_to='pics/pythi') # upload_to is loaction where to save images
    Offer=models.BooleanField(default=False)

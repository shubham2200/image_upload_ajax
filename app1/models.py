from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.

class user_image(models.Model):
    user_name = models.CharField(max_length=25 , null=True , blank= True)
    image = models.ImageField(upload_to = 'image/' ,blank= True , null= True)

    def __str__(self):
        return str(self.user_name)
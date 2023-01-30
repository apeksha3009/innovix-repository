from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=70) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image

class CustomUser(AbstractUser):
    designation=models.CharField(max_length=100, blank=True)
    profile_pic=models.ImageField(blank=True, null=True, default='default.png')

    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.profile_pic)
        # set self.image to new_image
        self.profile_pic = new_image
        # save
        super().save(*args, **kwargs)
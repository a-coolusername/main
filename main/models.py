from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class TAGinfo(models.Model):
    objects = models.Manager
    tag_NAME = models.CharField(max_length=255, null=False, blank=False)
    USERID = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    lastupdate = models.DateTimeField(null=True, blank=True, auto_now=True)



class ARTICLEinfo(models.Model):
    objects = models.Manager
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.CharField(max_length=255, null=True, blank=False)
    image = models.ImageField(upload_to='files/images')
    tags_associated = models.ManyToManyField(TAGinfo)
    USERID = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    lastupdate = models.DateTimeField(null=True, blank=True, auto_now=True)
    isactive = models.BooleanField(default=0)

from __future__ import unicode_literals

from django.db import models


# Create your models here.

class gmgallery(models.Model):
    title = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field="width", height_field="height",
                              upload_to='media/myphoto')
    #timestamp = models.DateTimeField(auto_now_add=True, auto_now_=False)
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
       ordering = ["title"]

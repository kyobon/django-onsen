from django.db import models
from stdimage.models import StdImageField

class Onsen(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    efficacy = models.CharField(max_length=500)
    skin = models.CharField(max_length=100)
    quality = models.CharField(max_length=100)
    image = StdImageField(upload_to='', variations={'sizea':(200,150),'sizeb':(400,300)})

    def __str__(self):
        return str(self.name)
from django.db import models


# this is really a dummy model class, so I can attach comments to something if I need to 

class SiteSettings(models.Model):
    homepage_meta_description = models.CharField(max_length=200)
    homepage_meta_title = models.CharField(max_length=200)
    
# Create your models here.

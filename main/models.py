from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

app_name = 'main'

# Create your models here.
class tag (models.Model): 
    word = models.CharField(max_length=35)
    slug = models.CharField(max_length=250)
    Created_at = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __unicode__(self):
        return self.word

class tintuc(models.Model): 
    id = models.IntegerField(primary_key=True)
    TenBai = models.CharField(max_length=500)
    noidung = RichTextUploadingField()    
    ngaygio = models.DateTimeField(auto_created=True, auto_now_add=True)
    image = models.ImageField()
  
    def __str__(self): 
        return self.TenBai


    def get_absolute_url(self): 
        return reverse("newsdetail", kwargs={'pk': self.pk})
    
    
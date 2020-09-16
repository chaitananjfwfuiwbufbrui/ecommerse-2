from django.db import models
from django.db.models.signals import pre_save
from app.utils import unique_slug_generator
# Create your models here.
class products(models.Model):
    product_id = models.AutoField
    product_name = models.CharField( max_length=50)
    prize = models.IntegerField(default=0)
    category = models.CharField(max_length=50,default="")
    sub_category = models.CharField(max_length=50,default="")
    product_image =models.ImageField(upload_to="shop/images",default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    slug = models.SlugField(blank=True,null=True)
    



    def __str__(self):
        return self.product_name +" catagiory:   " +self.category

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=products)
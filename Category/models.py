from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    category  = models.CharField(max_length = 200,unique = True)
    slug = models.SlugField(max_length =500)
    description = models.CharField(max_length =255,blank = True)
    cast_image =models.ImageField(upload_to='photos/categories',blank= True)

    class Meta :
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('product_by_category', args =[self.slug])

    def __str__(self):
        return self.category                     
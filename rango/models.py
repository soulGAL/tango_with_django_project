from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)#这个字段是用来创建友好的URL的

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):#定义了一个__str__()方法，它返回了一个字符串，这个字符串是一个Category对象的名字
        return self.name



class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self):#定义了一个__str__()方法，它返回了一个字符串，这个字符串是一个Page对象的名字
        return self.title
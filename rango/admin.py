from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from rango.models import Category, Page

class CategoryAdmin(ModelAdmin):#这个类继承了ModelAdmin类，它允许我们自定义admin界面
    prepopulated_fields = {'slug': ('name',)}#这个字段是用来创建友好的URL的

class PageAdmin(ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Category)
admin.site.register(Page, PageAdmin)







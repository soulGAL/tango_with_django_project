from django import template
from rango.models import Category

register = template.Library()#创建一个template.Library类的实例，它将被用来注册自定义的模板标签和过滤器

@register.inclusion_tag('rango/categories.html')#inclusion_tag()装饰器告诉Django这个函数是一个模板标签
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
            'current_category': current_category}
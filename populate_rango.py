import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'tango_with_django_project.settings') # 这是为了让django能够找到settings.py文件

import django
django.setup()
from rango.models import Category, Page

def populate():
    # 首先，我们将创建字典列表，其中包含我们要添加到每个类别中的页面。
    #  然后我们将为我们的类别创建一个字典字典。
    #  这可能看起来有点混乱，但它允许我们遍历每个数据结构，并将数据添加到我们的模型中。
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/'} ]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/'} ]

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask',
        'url':'http://flask.pocoo.org'} ]

    cats = {('Python', 128, 64): {'pages': python_pages},
            ('Django', 64, 32): {'pages': django_pages},
            ('Other Frameworks', 32, 16): {'pages': other_pages} }

# If you want to add more categories or pages,
# add them to the dictionaries above.

# The code below goes through the cats dictionary, then adds each category,
# and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():# 这里的cat是字典的key，cat_data是字典的value
        #cat元组依次作为参数传入add_cat函数
        c = add_cat(cat[0], cat[1], cat[2])
        for p in cat_data['pages']:# 这里的p是一个字典
            add_page(c, p['title'], p['url'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]# 这里的p是一个Page对象
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]# 这里的c是一个Category对象,
    c.views = views
    c.likes = likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
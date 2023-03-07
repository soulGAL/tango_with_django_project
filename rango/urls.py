from django.urls import path
from rango import views

app_name = 'rango'
urlpatterns = [
    #访问rango/时，留下的空字符串, 调用views.index函数
    path('', views.index, name='index'),
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),#name='show_category'是给这个URL起的名字
    path('add_category/', views.add_category, name='add_category'),



]
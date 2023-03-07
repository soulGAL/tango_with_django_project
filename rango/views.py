from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]#[:5]是切片操作，取前5个元素

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)#context=context_dict是上下文字典


def about(request):
    # prints out whether the method is a GET or a POST
    print(request.method)
    # prints out the user name, if no one is logged in it prints `AnonymousUser`
    print(request.user)
    return render(request, 'rango/about.html', {})#{}是上下文字典,这里为空,因为没有传递任何变量给模板



def show_category(request, category_name_slug):#category_name_slug是一个字符串
    # 创建一个上下文字典，我们可以将它传递给模板引擎
    context_dict = {}
    try:
        # 试着从数据库中获取一个与slug名字匹配的category对象
        # 我们可以使用get()方法，因为我们知道category_name_slug是唯一的
        # 如果没有找到指定的category对象，get()方法会抛出一个DoesNotExist异常
        category = Category.objects.get(slug=category_name_slug)#category_name_slug是一个字符串
        # 从数据库中获取与这个category相关联的所有页面
        # 注意，filter()返回一个page对象列表或空列表
        pages = Page.objects.filter(category=category)#filter()方法返回的是一个QuerySet对象
        # 将我们从数据库中获取的列表添加到上下文字典中
        context_dict['pages'] = pages
        # 我们还把从数据库中获取的category对象添加到上下文字典中
        # 我们将在模板中使用它来确认category对象是否存在
        context_dict['category'] = category
    except Category.DoesNotExist:
        # 我们在这里没有找到指定的category对象
        # 不需要做什么事情
        # 模板将显示“没有找到指定的category”信息
        context_dict['category'] = None
        context_dict['pages'] = None

    # 前面的代码和前面的视图函数一样
    # 现在我们渲染响应并将上下文字典传递给模板引擎
    return render(request, 'rango/category.html', context=context_dict)


def add_category(request):
    form = CategoryForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            return index(request)
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})
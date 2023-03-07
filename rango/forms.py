from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
    help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

# An inline class to provide additional information on the form.
    class Meta:
    # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
    help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
    help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        #我们希望在表单中包含哪些字段？这样我们就不需要模型中的每个字段都存在。
        # 某些字段可能允许 NULL 值；我们可能不想包括它们。在这里，我们隐藏了外键。
        # 我们可以从表单中排除类别字段，
        exclude = ('category',)
#or specify the fields to include (don't include the category field).
#fields = ('title', 'url', 'views')
    def clean(self):
        cleaned_data = self.cleaned_data #cleaned_data是一个字典, 里面包含了表单中的数据
        url = cleaned_data.get('url')#get()方法返回字典中指定键的值
        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'):#startswith()方法检查字符串是否是以指定子字符串开头
            url = f'http://{url}'
            cleaned_data['url'] = url
            return cleaned_data
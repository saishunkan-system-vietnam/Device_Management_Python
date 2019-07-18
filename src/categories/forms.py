from .models import Categories
from ..brands.models import brands
from django import forms
from django.forms import ModelForm



class CategoriesForm(forms.ModelForm):

    category_name = forms.CharField(
        label="Name", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Categories
        fields = ['id_parent', 'category_name', 'brands_id', ]

    def clean(self):
        super().clean()
        category_name = self.cleaned_data.get('category_name')
        if len(category_name) > 100:
            self.errors['category_name'] = self.error_class(['Không được nhập quá 100 ký tự.'])
        if not category_name:
            self.errors['category_name'] = self.error_class(['Category name là bắt buộc.'])
        id_parent = int(self.cleaned_data.get('id_parent'))
        if (not id_parent or id_parent == None) & id_parent != 0:
            self.errors['id_parent'] = self.error_class(['Category parent là bắt buộc.'])
        brands_id = self.cleaned_data.get('brands_id')
        if not brands_id or brands_id == None:
            self.errors['brands_id'] = self.error_class(['Brands là bắt buộc'])
        return self.cleaned_data

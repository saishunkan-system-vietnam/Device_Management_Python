from .models import brands
from django.forms import ModelForm
from django import forms


class BrandForm(forms.ModelForm):
    error_css_class = 'error'
    brand_name = forms.CharField(label='Brand name:', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = brands
        fields = ['brand_name']

    def clean(self):
        super().clean()
        brand_name = self.cleaned_data.get('brand_name')
        if len(brand_name) > 10:
            # self._errors['brand_name'] = self.error_class(['Không được nhập quá 10 kí tự'])
            self.add_error('brand_name', 'Không được nhập quá 10 kí tự')
        if brand_name.__contains__('n') == False:
            # self._errors['brand_name'] = self.error_class(['Chưa có kí tự n'])
            self.add_error('brand_name', 'Chưa có kí tự n')
        return self.cleaned_data

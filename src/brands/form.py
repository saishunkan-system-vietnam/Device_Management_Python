from .models import brands
from django.forms import ModelForm
from django import forms


class BrandForm(forms.ModelForm):
    brand_name = forms.CharField(label='Brand name:', max_length = 100,  widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = brands
        fields = ['brand_name']
    

    def clean(self):
        super().clean()
        brand_name = self.cleaned_data.get('brand_name')
        if len(brand_name) > 100:
            self._errors['brand_name'] = self.error_class(['Không được nhập quá 100 kí tự'])
            # self.add_error('brand_name', 'Không được nhập quá 10 kí tự')
        if not brand_name:
            self._errors['brand_name'] = self.error_class(['Không được phép để trống.'])
            # self.add_error('brand_name', 'Chưa có kí tự n')
        return self.cleaned_data

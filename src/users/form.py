from .models import Users
from django.forms import ModelForm
from django import forms
import re

class UserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['email']

    def clean(self):
        super().clean()
        email = self.cleaned_data['email']
        reg = re.compile('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$')
        if not reg.match(email) :
            raise forms.ValidationError(u'%s Invalid email address ' % email)
        # if Users.objects.filter(email=email).exists():
        #     raise forms.ValidationError("Email already exists")
        # return email

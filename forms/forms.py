from django import forms


class UserInfoForm(forms.Form):
    first_name = forms.CharField(max_length=64, required=True)
    last_name = forms.CharField(max_length=64, required=False)
    image = forms.ImageField(required=True)

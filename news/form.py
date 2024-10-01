from django import forms
from news.models import ContactModel, NewsletterModel


class ContactModelForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email']

        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('This field should be email')
        return email

    class Meta:
        model = ContactModel
        fields = ('full_name', 'email', 'subject', 'message')
        # exclude = ('created_at', 'updated_at',)


class NewsletterModelForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email']

        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('This field should be email')
        return email

    class Meta:
        model = NewsletterModel
        fields = ('email',)


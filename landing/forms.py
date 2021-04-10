from django import forms

from landing.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Your Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Your Email', 'required': True}),
            'subject': forms.TextInput(attrs={'class': 'form-control',
                                              'required': True, 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Message', 'required': True})
        }

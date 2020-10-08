from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100, required=True)
    email = forms.EmailField(label='Your email address', required=True)
    subject = forms.CharField(label='Subject',required = False)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
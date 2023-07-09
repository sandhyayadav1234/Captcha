from django import forms
from captcha.fields import CaptchaField
class ContactForm(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    cap=CaptchaField()


from django import forms
from .models import CommentModel
from captcha.fields import CaptchaField


class CommentForms(forms.ModelForm):
    name = forms.CharField(max_length=120,
                           widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your name ...'}))

    subject = forms.CharField(max_length=120,
                              widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'Enter your subject ...'}))
    email = forms.EmailField(widget=forms.widgets.EmailInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'Enter your email ...'}))
    text = forms.CharField(max_length=5000,
                           widget=forms.widgets.Textarea(attrs={'class': 'form-control',
                                                                'placeholder': 'Enter your comment ...'}))
    captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invaid': 'Неправильный текст'})

    class Meta:
        model = CommentModel
        fields = ('name', 'subject', 'email', 'text', 'captcha')

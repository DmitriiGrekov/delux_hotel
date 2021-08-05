from django import forms
from .models import RoomModelReserved


class RoomModelReservedForm(forms.ModelForm):
    first_name = forms.CharField(max_length=120,
                                 widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Enter your name ...'}))
    last_name = forms.CharField(max_length=120,
                                widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Enter your surname ...'}))
    email = forms.EmailField(widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Enter your email ...'}))
    phone_number = forms.CharField(max_length=30,
                                   widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                         'type': 'tel',
                                                                         'placeholder': 'Enter your phone ...'}))
    additional_node = forms.CharField(max_length=1000,
                                      widget=forms.widgets.Textarea(attrs={'class': 'form-control',
                                                                           'placeholder': 'Type here ...'}))

    class Meta:
        model = RoomModelReserved
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'additional_node')

from django import forms
from .models import ContactMessageModel


class ContactMessageForm(forms.ModelForm):
    name = forms.CharField(max_length=120,
                           widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your name ...'}))
    surname = forms.CharField(max_length=120,
                              widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'Enter your surname ...'}))
    phone = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Enter your phone...'}))
    note = forms.CharField(max_length=500, widget=forms.widgets.Textarea(attrs={'class': 'form-control',
                                                                                'placeholder': 'Additional note type here ...',
                                                                                'rows': '10'}))

    class Meta:
        model = ContactMessageModel
        fields = ('name', 'surname', 'phone', 'note')

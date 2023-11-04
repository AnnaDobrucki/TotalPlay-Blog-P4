from .models import *
from django import forms
from django.core import validators
from django.forms import ModelForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class DateInput(forms.DateInput):
    """
    Inputs a widget on the form for date selection
    """
    input_type = 'date'


class OnlineForm(ModelForm):
    """
   Creates Placeholders/ widgets for relevant data input
   sections, and links to view.py to give
   the fields for booking
   """
    name = forms.CharField(
        label='Booking Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Booking Name'}),
    )

    email_address = forms.EmailField(
        label='Email Address',
        required=True,
        validators=[validators.EmailValidator(message="Invalid Email")],
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'}),
    )

    phone = forms.IntegerField(
        label='Contact Number',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}),
    )

    class Meta:

        model = Booking
        fields = '__all__'
        exclude = ('user', )
        widgets = {
            'date': DateInput()
        }
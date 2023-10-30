from .models import *
from django import forms
from django.core import validators
from django.forms import ModelForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class DateInput(forms.DateInput):
    input_type = 'date'


class OnlineForm(ModelForm):

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
        # All fields to be used
        fields = '__all__'
        # Apart for the user field
        exclude = ('user', )
        widgets = {
            'date': DateInput()
        }
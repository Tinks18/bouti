from django import forms
from django.forms import ModelForm
from .models import Contact, Post, Response
from django_summernote.widgets import SummernoteWidget


class ContactForm(ModelForm):
    """
    Contact form
    """
    class Meta:
        model = Contact
        fields = '__all__'


class ResponseForm(forms.ModelForm):

    class Meta:
        model = Response
        fields = ('body',)

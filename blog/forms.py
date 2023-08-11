from django import forms
from django.forms import ModelForm
from .models import Contact, Post, Response, Review
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


class ReviewForm(forms.ModelForm):
    """ Form to create review """
    class Meta:
        model = Review
        fields = ['title', 'product_name', 'content', 'rating']
        content = forms.CharField(widget=SummernoteWidget())

        labels = {
            'title': 'Review Title',
            'product_name': 'Product Name',
            'content': 'Review',
            'rating': 'Rating'
        }
import django_filters
from django_filters import CharFilter
from django import forms
from core.models import *


class PostFilter(django_filters.FilterSet):
    headline = CharFilter(field_name='headline',
                          lookup_expr="icontains", label='Headline')

    class Meta:
        model = Post
        fields = ['headline', 'body']

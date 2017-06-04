# coding: utf-8
import re
from django import forms
from django.forms.utils import ErrorList
from .models import Cuento


class CuentosForm(forms.modelForm):
    class Meta:
        model = Cuento
        exclude = 'created_at'

from django import forms
from .models import TextInput

class TextInputForm(forms.ModelForm):
    class Meta:
        model = TextInput
        fields = '__all__'
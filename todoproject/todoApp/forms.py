from .models import Tasks
from django import forms
class TodoForms(forms.ModelForm):
    class Meta:
        model=Tasks
        fields=['name','priority','date']
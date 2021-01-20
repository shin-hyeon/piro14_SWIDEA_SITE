from django import forms
from .models import Idea, DevTool

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = '__all__'

class DevForm(forms.ModelForm):
    class Meta:
        model = DevTool
        fields = '__all__'

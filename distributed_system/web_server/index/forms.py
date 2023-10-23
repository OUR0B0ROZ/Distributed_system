from django import forms
from .code_generator import generate_code
from .models import  ModelTest
class ModelTestAdminForm(forms.ModelForm):
    class Meta:
        model = ModelTest
        fields = '__all__'

    code = forms.CharField(
        label='Preview Code',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
        initial=generate_code()
    )
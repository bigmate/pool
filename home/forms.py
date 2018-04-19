from django import forms
from .models import Ad
class Post(forms.ModelForm):
    class Meta:
        model = Ad
        exclude = ('pub_date','lookups','user',)
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'region': forms.Select(attrs={'class':'custom-select my-1 mr-sm-2'}),
            'metro': forms.Select(attrs={'class':'custom-select my-1 mr-sm-2'}),
            'category': forms.Select(attrs={'class': 'custom-select my-1 mr-sm-2'}),
            'desc': forms.Textarea(attrs={'class':'form-control','rows':'3'}),
            'is_paid': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'image': forms.FileInput(attrs={'class':'custom-file-input', 'multiple':False})
        }
from django import forms

from userprofile.models import MyUser


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('avatar', 'first_name',)

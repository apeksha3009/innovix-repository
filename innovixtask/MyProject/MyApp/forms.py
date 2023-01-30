from .models import CustomUser
from django import forms

class CustomUserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields=('first_name', 'last_name', 'username', 'password', 'designation', 'profile_pic')

    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class CustomUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields=('first_name', 'last_name', 'username', 'designation', 'profile_pic')
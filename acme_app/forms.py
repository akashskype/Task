from django import forms
from .models import Department, User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'department')


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        exclude = ('created_by', 'last_updated_at')


class AssignDepartmentForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('department',)



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


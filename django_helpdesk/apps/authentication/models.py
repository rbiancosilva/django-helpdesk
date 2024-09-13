from django import forms

ROLES = {
    "OPR":"Operator",
    "USR":"User",
}


class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=60)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    role = forms.CharField(
        max_length=4,
        widget=forms.Select(choices=ROLES)
    )
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())





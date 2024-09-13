from django import forms

ROLES = {
    "OPR":"Operator",
    "USR":"User",
}


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=60, required=True)
    email = forms.EmailField(required=True)
    role = forms.CharField(
        max_length=4,
        widget=forms.Select(choices=ROLES),
        required=True,
    )
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(),required=True)

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)





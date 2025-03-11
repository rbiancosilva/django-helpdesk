from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=60, required=True)
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)





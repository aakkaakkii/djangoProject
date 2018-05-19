from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

User = get_user_model()


class NameForm(forms.Form):
    title = forms.CharField(label='title', max_length=50)
    text = forms.CharField(label='text', max_length=500)


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("incorrect password")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

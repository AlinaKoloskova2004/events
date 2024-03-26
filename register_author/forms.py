from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    password1 = forms.CharField(max_length=255)
    password2 = forms.CharField(max_length=255)


    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.surname = self.cleaned_data['surname']
        user.name = self.cleaned_data['name']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        user.save()
        return user


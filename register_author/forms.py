from allauth.account.forms import SignupForm as AllauthSignupForm
from django import forms

class SignupForm(AllauthSignupForm):
    surname = forms.CharField(max_length=30, label='Имя')
    name = forms.CharField(max_length=30, label='Фамилия', required=False)

    def save(self, request):
        user = super(SignupForm, self).save(request)
        user.surname = self.cleaned_data['surname']
        user.name = self.cleaned_data['name']
        user.save()
        return user
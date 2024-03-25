from django.contrib.auth import get_user_model
from allauth.account.views import SignupView
from django.shortcuts import render

class CustomSignupView(SignupView):
    template_name = 'account/signup.html'
    form_class = CustomSignupForm

    def form_valid(self, form):
        response = super(CustomSignupView, self).form_valid(form)
        user = get_user_model().objects.get(email=form.cleaned_data['email'])
        user.is_active = False
        user.save()
        return response

def account_confirm(request):
    return render(request, 'account/confirm.html')

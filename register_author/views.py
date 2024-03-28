from django.contrib.auth import get_user_model
from allauth.account.views import SignupView
from django.shortcuts import render
from register_author.forms import CustomSignupForm
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    if request.method == 'POST':
            form = CustomSignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/confirm-email/')
        else:
            form = CustomSignupForm()

        return render(request, 'account/signup.html', {'form': form})

def account_confirm(request):
    return render(request, 'account/confirm.html')

def profile(request):
    if not request.user.is_authenticated or not request.user.email_confirmed:
        return redirect('confirm_email')
    else:
        return render(request, 'profile/profile.html')
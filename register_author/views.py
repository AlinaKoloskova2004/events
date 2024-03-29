

from allauth.account.views import SignupView
from .forms import SignupForm

class CustomSignupView(SignupView):
    form_class = SignupForm



def profile(request):
    if not request.user.is_authenticated or not request.user.email_confirmed:
        return redirect('confirm_email')
    else:
        return render(request, 'profile/profile.html')
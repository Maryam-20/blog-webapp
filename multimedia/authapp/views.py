from django.shortcuts import render
from django.contrib.auth import login
from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, CreatorProfile
from .forms import UserProfile_form, User_form

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def form_valid(self, form):
        # Save the user instance
        user = form.save()
        # Log the user in
        login(self.request, user)
        return super().form_valid(form)
    
@login_required
def my_profile(request, userid):
    userProfile = UserProfile.objects.all().filter(user_id = userid)
    print(userProfile)
    return render(request = request, template_name= "authapp/profile.html", context={"userprofile":userProfile})
    
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import UserRegisterForm, ProfileForm
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'user/profile.html')


class UpdateProfile(LoginRequiredMixin,UpdateView):
    model   =   Profile
    template_name   =   'user/profile.html'
    form_class  =   ProfileForm

    

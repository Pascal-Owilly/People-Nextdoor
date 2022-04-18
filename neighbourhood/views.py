from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

def index(request):
    return render(request, 'neighbourhood/index.html')

def register(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'neighbourhood/register.html', {'form': form})

@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'neighbourhood/profile.html', context)
 
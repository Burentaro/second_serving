from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
<<<<<<< HEAD
                                   request.FILES, 
=======
                                   request.FILES,
>>>>>>> 5e137b64a1f67d8abd4f5a8e73b38b516b5b1b84
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
<<<<<<< HEAD
            messages.success(request, f'Your account has been updated!')
=======
            messages.success(request, f'Your account has been updated.')
>>>>>>> 5e137b64a1f67d8abd4f5a8e73b38b516b5b1b84
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
<<<<<<< HEAD
=======
    
>>>>>>> 5e137b64a1f67d8abd4f5a8e73b38b516b5b1b84
    context =  {
            'u_form': u_form,
            'p_form': p_form
            }
    
    return render(request, 'users/profile.html', context)
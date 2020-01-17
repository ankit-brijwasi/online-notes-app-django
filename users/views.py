from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, PasswordUpdateForm
from . models import Profile
from notes.models import Notes

@login_required
def home(request):
    notes = Notes.objects.filter(user=request.user).order_by('created_on')[0:3]
    return render(request, 'users/home.html', {
        'title': f'{request.user.username} Home',
        'home': 'active',
        'notes':notes
    })

@login_required
def settings(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated')
            return redirect("settings")
    else:
        u_form = UserUpdateForm(initial={
            'email': request.user.email,
            'firstname': request.user.first_name,
            'lastname': request.user.last_name,
            'username': request.user.username,
        })
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'settings': 'active',
        'u_form': u_form,
        'p_form': p_form,
        'notes': Notes.objects.filter(user=request.user)
    }
    return render(request, "users/settings.html", context)

@login_required
def changePassword(request):
    if request.method == "POST":
        form = PasswordUpdateForm(request.POST)
        # form = PasswordUpdateForm(user=request.user, data=request.POST)
        if form.is_valid():
            oldPass = request.POST.get('OldPassword', '')
            newPass = request.POST.get('NewPassword', '')
            confirmNewPass = request.POST.get('ConfirmPassword', '')
            if newPass != confirmNewPass:
                messages.warning(request, f'The passwords Didn\'t Match')
                return redirect('settings')
            else:
                pwd = request.user.password
                if check_password(oldPass, pwd):
                    request.user.set_password(newPass)
                    request.user.save()
                    # update_session_auth_hash(request.user, form.user)
                    messages.success(request, f'Password Changed! Please Log In again to continue')
                    # return redirect('settings')
                else:
                    messages.warning(request, f'Old Password is wrong!')
                    return redirect('settings')
    else:
        form = PasswordUpdateForm()

    return render(request, "users/change-password.html", {'form': form, 'settings': 'active'})
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can now log in')
            return redirect("user-login")
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'title': 'Register','form': form})
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Profile
from django.contrib import messages
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    back = redirect('/')
                    return HttpResponse(
                        f'Uwierzytelnienie {user.username} zakończyło się sukcesem. \n<a href="/">Kliknij by powrócić na główną</a>')
                else:
                    return HttpResponse('Nieprawidłowe logowanie')
            else:
                return HttpResponse('Nieprawidłowe dane')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


@login_required
def profile(request):
    context = {
        'section': 'profile',
    }
    return render(request, 'profile.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            context = {
                'new_user': new_user
            }
            return render(request, 'register_done.html', context)
    if request.user.is_authenticated:
        return redirect('/')
    else:
        user_form = UserRegistationForm()
    context = {
        'user_form': user_form
    }
    return render(request, 'register.html', context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Zaktualizowanie wykonane')
        else:
            messages.error(request, 'Wystapił błąd')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'edit.html', context)


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request,
                  'account/user/list.html',
                  {'section': 'people',
                   'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
                             username=username,
                             is_active=True)
    return render(request,
                  'account/user/detail.html',
                  {'section': 'people',
                   'user': user})

from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.db.models.signals import post_save
from .signals import create_profile, save_profile

from home.models import Posts
from users.models import Profile
# Create your views here.

def register(request):

    if request.method == 'POST':
        registerform = UserRegisterForm(request.POST) 
        
        if registerform.is_valid():
            registerform.save()

            post_save.connect(create_profile, sender=User)
            post_save.connect(save_profile, sender=User)


            
            username = registerform.cleaned_data.get('username')
            messages.success(request, "Your Account has been created!")

            return redirect('blog-login')
    else:
        registerform = UserRegisterForm()
    
    return render(request, 'users/register.html',{'registerform': registerform })


def profile(request,authorname=None):

    u = User.objects.filter(username=authorname)
    p = Profile.objects.filter(username=u[0])[0]

    return render(request, 'users/profile.html',{'posts':Posts.objects.filter(author=u[0]),'profile': p})



def updateprofile(request):
    if(request.method == 'POST'):
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Profile has been Updated!')
            redirect('blog-updateprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/updateprofile.html',context)



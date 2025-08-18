from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# from posts.models import Post
from .models import Profile
from .forms import CreateProfile
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/users/login')
# def users(request):
#     return render(request, 'usersPage.html')


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return render(request, 'signup.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # form2 = CreateProfile(request.POST)
        if form.is_valid():
            user = form.save()
            s = request.POST.dict()
            # instance = form2.save(commit=False)
            iname = s['username']
            # instance.name = str(s.username)
            # instance.user_slug = str(instance.name).strip()
            instance = Profile(name=iname , user_slug=iname.strip())
            instance.save()
            login(request, user)
            # return redirect('shop')
            return render(request, 'signup.html', {'form': form})
            
    form = CreateProfile()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('shop')


# @login_required(login_url='/users/login')
# def profile(request, slug):
#     posts = Post.objects.all()
#     form = Profile.objects.get(user_slug=slug)
#     our_name = str(Profile.objects.get(name=request.user))
#     is_following = bool(Follow.is_following)
#     return render(request, 'profile.html',
#                   {'form': form, 'posts': posts, 'our_name': our_name, 'is_following': is_following})



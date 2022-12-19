from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import post
from .forms import signupform, loginform, postform
from django.contrib.auth.models import Group

# Create your views here.

#home
def home(request):
    posts = post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})

#about
def about(request):
    return render(request, "blog/about.html")

#contact
def contact(request):
    return render(request, "blog/contact.html")

#dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        grps = user.groups.all()
        return render(request, "blog/dashboard.html", {"posts":posts, "full_name": full_name, "groups": grps})
    else:
        return HttpResponseRedirect("/login/")

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

#signup
def user_signup(request):
    if request.method == "POST":
        form = signupform(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations! You have become a Blogger, Upload your first blog.")
            user = form.save()
            # add user in Group (Blogger)
            group = Group.objects.get(name="Blogger")
            user.groups.add(group)
    else:
        form = signupform()
    return render(request, "blog/signup.html", {"form":form})

#login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = loginform(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data["username"]
                upass = form.cleaned_data["password"]
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully !")
                    return HttpResponseRedirect("/dashboard/")
        else:
            form = loginform()
        form = loginform()
        return render(request, "blog/login.html", {"form": form})
    else:
        return HttpResponseRedirect("/dashboard/")


# add new post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = postform(request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"]
                desc = form.cleaned_data["description"]
                pst = post(title=title, description=desc)
                pst.save()
                form = postform()
        else:
            form = postform()
        return render(request, "blog/addpost.html", {"form":form})
    else:
        return HttpResponseRedirect("/login/")


# update post
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pupdate = post.objects.get(pk=id)
            form = postform(request.POST, instance=pupdate)
            if form.is_valid():
                form.save()
        else:
            pupdate = post.objects.get(pk=id)
            form = postform(instance=pupdate)
        return render(request, "blog/updatepost.html", {"form":form})
    else:
        return HttpResponseRedirect("/login/")


# delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pd = post.objects.get(pk=id)
            pd.delete()
        return HttpResponseRedirect("/dashboard/")
    else:
        return HttpResponseRedirect("/login/")


from django.shortcuts import render,redirect,get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect

from django.template import loader

from django.urls import reverse


from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm,PostForm,EditPostForm

from .models import Post,Comment


from django.contrib.auth.models import User
 
from django.contrib import messages


def login_view(request):
    userform=UserLoginForm()
    context={'form':userform}
    return render(request,"login.html",context)


from django.contrib.auth.models import auth

def authenticate(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        #print(user)
        if user is not None:
            auth.login(request,user)
            #IF LOGIN WORKS GO TO THE FOLLWING PAGE
            #return redirect('/social_media/homepage/')#WAS
            return redirect('/social_media/images/')
            #return HttpResponse("POST METHOD")
        else:
            messages.info(request,'Invalid Username and Password.Please Try Again!')
            return redirect('login')
            #return HttpResponse("Invalid Credentials.Inside request")
    else:
        #redircet to login page again'
        return HttpResponse("Invalid Credentials.Outside request.Method not Allowed")

from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect('login')

#CREATE NEW USER
from .forms import AddUserForm

def add_user(request):
    userform=AddUserForm()
    context={'form':userform}
    return render(request,"add_user.html",context)

def validate(request):
    if request.method == 'POST':
        username = request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect("add_user")

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists. Please use a different email id to Sign-up.')
                return redirect("add_user")

                #return HttpResponse("Username already exists")
            else:  
                user = User.objects.create_user(username=username,email=email,password=password)
                user_login=auth.authenticate(request, username=username, password=password)
                UserProfile.objects.create(user=user)
                auth.login(request,user)
                #Message
                messages.info(request,'Welcome New User #Message')

                #GO TO MAINPAGE IF AUTHENTICIFICATION SUCCESSFUL
                return redirect('/social_media/images/')
                #return redirect('/social_media/homepage/')
        else:
            messages.info(request,'Passwords not matching')
            return redirect("add_user")

            #return HttpResponse("Password not matching")
    else:
        return HttpResponse("Method Not Allowed")

#NEWCODE

@login_required(login_url="login")
def homepage_view(request):
    if request.method == 'POST':
        # Check if the form is for a status post or an image post
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = Post(user=request.user, content=post_form.cleaned_data['content'])
            new_post.save()
            return redirect('homepage')
    else:
        post_form = PostForm()
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'post_form': post_form,
        'posts': posts,}
    return render(request, 'homepage.html', context)

    

from django.utils import timezone
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user == post.user:
        if request.method == 'POST':
            post_form = EditPostForm(request.POST)
            if post_form.is_valid():
                post.content = post_form.cleaned_data['content']
                post.date_posted = timezone.now()
                post.save()
                return redirect('homepage')
        else:
            post_form = EditPostForm(initial={'content': post.content})

        context = {
            'post_form': post_form,
            'post': post,
        }
        return render(request, 'edit_post.html', context)
    else:
        return redirect('homepage')

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user == post.user:
        post.delete()
        return redirect('homepage')
    else:
        # Handle unauthorized deletion (e.g., show an error message)
        return redirect('homepage')
#COMMENTS

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_text = request.POST.get('comment_text', '')
    if comment_text:
        Comment.objects.create(post=post, user=request.user, text=comment_text)
    return redirect('homepage')
    
@login_required
def delete_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    # Check if the logged-in user is the author of the comment
    if request.user == comment.user:
        comment.delete()

    return redirect('homepage')


#IMAGE HANDLING FEATURES
from .forms import ImageForm
from .models import Image,ImageComment

@login_required(login_url="login")
def images(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)
            image_instance.user = request.user
            image_instance.save()
            obj = form.instance
            return redirect('images')
    else:
        form = ImageForm()
        img = Image.objects.all().order_by('-id')

    return render(request, "template.html", {"img": img, "form": form})

@login_required
def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('images')
    return redirect('images')
   
@login_required
def add_image_comment(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    comment_text = request.POST.get('comment_text', '')
    if comment_text:
        ImageComment.objects.create(post=image,user=request.user, text=comment_text)
    return redirect('images')

@login_required
def delete_image_comment(request, image_id, comment_id):
    image = get_object_or_404(Image, pk=image_id)
    comment = get_object_or_404(ImageComment, pk=comment_id)
    comment.delete()
    return redirect('images')

@login_required
def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'image_detail.html', {'image': image})


# views.py
from .models import UserProfile
from .forms import UserProfileForm

@login_required(login_url="login")
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'user_profile.html', {'user': user, 'profile_form': profile_form, 'profile': profile})

@login_required(login_url="login")
def update_profile_picture(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get_or_create(user=user)[0]

    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', username=username)
    else:
        form = ProfilePictureForm(instance=profile)

    return render(request, 'update_profile_picture.html', {'user': user, 'profile': profile, 'form': form})
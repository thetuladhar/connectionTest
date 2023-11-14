from django.shortcuts import render,redirect

from django.http import HttpResponse,HttpResponseRedirect

from .models import Question

from django.template import loader

from django.urls import reverse


from django.contrib.auth.decorators import login_required

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# import datetime
# import random

# quotes=[
#     "May the Force be with you. - Star Wars",
#     "There's no place like home. - The Wizard of Oz",
#     "You can't handle the truth! - A Few Good Men",
#     "I'll be back. - The Terminator"
# ]
# def first_view(request):
#     return HttpResponse("First View.")

# def date_time(request):
#     current_datetime = datetime.datetime.now()
#     formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
#     return HttpResponse(formatted_datetime)

# def random_quote(request): 
#     random_line = random.choice(quotes)
#     return HttpResponse(random_line)

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    #exclude_list
    #filter
    #return HttpResponse(output)

    template = loader.get_template("index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

  


def detail(request, question_id):
    question_object=Question.objects.get(id=question_id)
    # print(question_object)
    # return HttpResponse("You're looking at question %s." % question_id)
    context = {
    "question": question_object
    }

    return render(request,"detail.html", context)

# question_obj = Question.objects.get(id=question_id)
#     context = {
#         "question": question_obj
#     }
 
#     return render(request,"detail.html", context)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("results", args=(question.id,)))


from django.shortcuts import get_object_or_404

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


from .forms import UserLoginForm

def login_view(request):
    userform=UserLoginForm()
    context={
        'form':userform
    }
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
            #redirect to app
            #IF LOGIN WORKS GO TO THE FOLLWING PAGE
            return redirect('/first_project/welcome')
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
def check_logged_in(request):
     return HttpResponse("USER LOGGED IN!")

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect('login')


#CREATE NEW USER

from .forms import AddUserForm

def add_user(request):
    userform=AddUserForm()
    context={
        'form':userform
    }
    return render(request,"add_user.html",context)


from django.contrib.auth.models import User
 
from django.contrib import messages

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
                auth.login(request,user)

                #Message
                messages.info(request,'Welcome New User #Message')
                #GO TO MAINPAGE
                return redirect('/first_project/welcome/')
        else:
            messages.info(request,'Passwords not matching')
            return redirect("add_user")

            #return HttpResponse("Password not matching")
    else:
        return HttpResponse("Method Not Allowed")

#from django.contrib.auth.decorators import login_required

def welcome_view(request):
    userform=UserLoginForm()
    context={
        'form':userform
    }
    return render(request,"welcome.html",context)

@login_required(login_url="login",)
def restricted_view(request):
    #messages.info(request,'Restricted Page Login Required.')
    userform=UserLoginForm()
    context={
        'form':userform
    }
    return render(request,"restricted.html",context)

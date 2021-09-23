from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Contactus, Likepost, Usercomment, Userquest
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# Views


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            question_data = request.POST.dict()
            textdata = question_data.get("question")

            print(question_data)
            userpost = Userquest(quest=textdata)
            userpost.author = request.user
            userpost.save()
            messages.success(request, "Successfully Posted!")

        snipps = Userquest.objects.all().order_by('-timestamp')

        return render(request, 'home.html', {'snipps': snipps})
    else:
        return redirect('/signup')


def contactushandle(request):
    if request.method == 'POST':
        contactus_data = request.POST.dict()
        name = contactus_data.get("name")
        email = contactus_data.get("email")
        message = contactus_data.get("message")

        contactus = Contactus(name=name, email=email, message=message)
        contactus.save()
        return redirect('/contactus')

    return render(request, 'contactus.html')


def handlepost(request, post_id):
    if request.user.is_authenticated:
        post_id_int = int(post_id)
        instance_post = Userquest.objects.get(id=post_id_int)
        if request.method == 'POST':
            comment_data = request.POST.dict()
            textdata = comment_data.get("yourcomment")

            print(textdata)
            print(instance_post.id)
            usercomment = Usercomment(comment=textdata)
            usercomment.post_id = instance_post
            usercomment.comment_author = request.user
            usercomment.save()
            messages.success(request, "Successfully Posted!")
        answer_lists = Usercomment.objects.filter(
            post_id=post_id_int).order_by('-timestamp')
        question = Userquest.objects.get(id=post_id_int)

        return render(request, 'post.html', {'answer_lists': answer_lists, 'question': question})

    else:
        return redirect('/signup')


def aboutus(request):
    return render(request, 'aboutus.html')


# APIs

def userauthenticate(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST' and 'btnform1' in request.POST:
            login_data = request.POST.dict()
            username = login_data.get("username")
            fname = login_data.get("f_name")
            lname = login_data.get("l_name")
            email = login_data.get("email")
            password = login_data.get("password")

            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()
            print(login_data)
            # messages.success(request, "Account Created Successfully")

        if request.method == 'POST' and 'btnform2' in request.POST:
            login_data = request.POST.dict()
            login_username = login_data.get("username")
            login_email = login_data.get("email")
            login_password = login_data.get("password")
            user = authenticate(username=login_username,
                                password=login_password)

            if user is not None:
                login(request, user)
                print("Login Success")
                return redirect('/')
            else:
                print("Invalid Login")
                return redirect('/signup')

        return render(request, 'login.html')


def userlogout(request):
    logout(request)
    print('logged out successfully')
    return redirect('/signup')


def deletepost(request, id):
    if request.user.is_authenticated:
        print(id)
        print('delete request sent')
        post = Userquest.objects.get(id=id)
        post.delete()
        messages.success(request, "Successfully Deleted!")
        return redirect('/')
    else:
        return redirect('/signup')


def likepost(request, post_id):
    instance_post = Userquest.objects.get(id=post_id)
    likepostobj, created = Likepost.objects.update_or_create(
        post_id=instance_post, user_id=request.user, defaults={'is_liked': 'True', 'is_disliked': 'False'})
    userquestobj = Userquest.objects.get(id=post_id)
    if userquestobj.dislike_count > 0:
        userquestobj.like_count += 1
        userquestobj.dislike_count -= 1
    else:
        userquestobj.like_count += 1
    userquestobj.save()

    return redirect('GetUserPost', post_id=post_id)


def dislikepost(request, post_id):
    instance_post = Userquest.objects.get(id=post_id)
    likepostobj, created = Likepost.objects.update_or_create(
        post_id=instance_post, user_id=request.user, defaults={'is_liked': 'False', 'is_disliked': 'True'})
    userquestobj = Userquest.objects.get(id=post_id)
    if userquestobj.like_count > 0:
        userquestobj.dislike_count += 1
        userquestobj.like_count -= 1
    else:
        userquestobj.dislike_count += 1
    userquestobj.save()

    return redirect('GetUserPost', post_id=post_id)

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, UserManager
import bcrypt

def index(request):
    return render(request, 'registration/index.html')

def register(request):
    errors = User.objects.user_reg_validation(request.POST)
    print 'error len', len(errors)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')
    else:
        new_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        print new_hash
        new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password_hash=new_hash)
        new_user.save()
        request.session['id'] = new_user.id
        return redirect('/success')

def success(request):
    try:
        request.session['id']
    except KeyError:
        return redirect('/')
    
    logged_in_user = User.objects.get(id=request.session['id'])
    context = {
        'user':logged_in_user
    }
    return render(request, 'registration/success.html', context)

def login_page(request):
    return render(request, 'registration/login.html')

def login(request):
    if len(request.POST['password']) < 1 or len(request.POST['email']) < 1:
        return login_fail(request)

    try:
        user_to_check = User.objects.get(email=request.POST['email'])
    except User.DoesNotExist:
        return login_fail(request)

    password = request.POST['password'].encode("utf-8")

    if bcrypt.checkpw(password, user_to_check.password_hash.encode("utf-8")):
        request.session['id'] = user_to_check.id
        return redirect('/success')
    else:
        return login_fail(request)

def login_fail(request):
    messages.error(request, "Login Failed")
    return redirect('/login')

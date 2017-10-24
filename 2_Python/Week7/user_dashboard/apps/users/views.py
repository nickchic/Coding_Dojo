from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Message, Comment
import bcrypt

def index(request):
    logged_in_user = get_logged_in_user(request)
    context = {
        'logged_in':logged_in(request)
    }
    return render(request, 'users/index.html', context)

def login_page(request):
    return render(request, 'users/login.html')

def login_action(request):
    if len(request.POST['password']) < 1 or len(request.POST['email']) < 1:
        return login_fail(request)

    try:
        user_to_check = User.objects.get(email=request.POST['email'])
    except User.DoesNotExist:
        return login_fail(request)

    password = request.POST['password'].encode("utf-8")

    if bcrypt.checkpw(password, user_to_check.password_hash.encode("utf-8")):
        request.session['id'] = user_to_check.id
        return redirect('/users/show/{}'.format(user_to_check.id))
    else:
        return login_fail(request)

def login_fail(request):
    messages.error(request, "Login Failed")
    return redirect('/login')

def register_page(request):
    return render(request, 'users/registration.html')

def register_action(request):
    errors = User.objects.user_validation(request.POST)
    print 'error len', len(errors)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/register')
    else:
        new_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        print new_hash
        new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password_hash=new_hash, admin=False)
        new_user.save()
        request.session['id'] = new_user.id
        return redirect('/users/show/{}'.format(new_user.id))

def new_user_page(request):
    logged_in_user = get_logged_in_user(request)
    content = {
        'logged_in':logged_in(request)
    }
    if not logged_in_user.admin:
        return redirect('/')
    return render(request, 'users/new_user.html', content)

def new_user_action(request):
    if 'admin' in request.POST:
        admin = True
    else:
        admin = False

    errors = User.objects.user_validation(request.POST)
    print 'error len', len(errors)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/users/new')
    else:
        new_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password_hash=new_hash, admin=admin)
        new_user.save()
        return redirect('/dashboard/admin')

def user_page(request, user_id):
    try:
        this_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('/')

    context = {
        'user':this_user,
        'logged_in':logged_in(request),
        'wall_messages':this_user.wall_messages.all().order_by('-created_at')
    }
    return render(request, 'users/user_page.html', context)

def this_user_page(request):
    if logged_in(request):
        return redirect('/users/show/{}'.format(get_logged_in_user(request).id))
    else:
        return redirect('/')

def user_dashboard(request):
    logged_in_user = get_logged_in_user(request)

    if logged_in_user == None:
        return redirect('/login')

    if logged_in_user.admin:
        return redirect('/dashboard/admin')

    users = User.objects.all()

    context = {
        'users':users,
        'user':logged_in_user,
        'logged_in':logged_in(request)
    }
    return render(request, 'users/dashboard.html', context)


def admin_dashboard(request):
    logged_in_user = get_logged_in_user(request)

    if logged_in_user == None:
        return redirect('/login')

    if not logged_in_user.admin:
        return redirect('/dashboard')

    users = User.objects.all()

    context = {
        'users':users,
        'logged_in_user':logged_in_user,
        'logged_in':logged_in(request)
    }
    return render(request, 'users/dashboard.html', context)

def edit_user_page(request):
    logged_in_user = get_logged_in_user(request)
    if logged_in_user == None:
        return redirect('/login')
    context = {
        'user':logged_in_user,
        'logged_in':logged_in(request)
    }
    return render(request, 'users/edit.html', context)

def edit_admin_page(request, user_id):
    logged_in_user = get_logged_in_user(request)

    if logged_in_user == None:
        return redirect('/login')

    if int(logged_in_user.id) == int(user_id):
        return redirect('/users/edit')

    if not logged_in_user.admin:
        return redirect('/')

    user = User.objects.get(id=user_id)

    context = {
        'user':user,
        'logged_in':logged_in(request)
    }
    return render(request, 'users/edit.html', context)

def edit_action(request, user_id):
    errors = User.objects.info_validation(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error)
        print 'edit error'
        return redirect('/users/edit/{}'.format(user_id))
    else:
        user_to_change = User.objects.get(id=user_id)
        user_to_change.first_name = request.POST['first_name']
        user_to_change.last_name = request.POST['last_name']
        user_to_change.email = request.POST['email']
        user_to_change.save()
        return redirect('/users/show/{}'.format(user_id))

def change_password(request, user_id):
    errors = User.objects.password_validation(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error)
        print 'edit error'
        return redirect('/users/edit/{}'.format(user_id))
    else:
        user_to_change = User.objects.get(id=user_id)
        new_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user_to_change.password_hash = new_hash
        user_to_change.save()
        return redirect('/dashboard')

def add_desc(request, user_id):

    if len(request.POST['desc']) < 1:
        messages.error(request, 'You left description blank!')
        return redirect('/users/edit/{}'.format(user_id))
    else:
        user_to_change = User.objects.get(id=user_id)
        user_to_change.desc = request.POST['desc']
        user_to_change.save()
        return redirect('/users/show/{}'.format(user_id))

def remove_user(request, user_id):
    user_to_delete = User.objects.get(id=user_id)
    user_to_delete.delete()
    return redirect('/dashboard/admin')

def post_message(request, user_id):
    if not len(request.POST['message']) < 1:
        recipient = User.objects.get(id=user_id)
        new_message = Message(text=request.POST['message'],author=get_logged_in_user(request), recipient=recipient)
        new_message.save()
    return redirect('/users/show/{}'.format(user_id))

def post_comment(request, user_id, message_id):
    if not len(request.POST['comment']) < 1:
        recipient = User.objects.get(id=user_id)
        new_comment = Comment(text=request.POST['comment'],author=get_logged_in_user(request), message=Message.objects.get(id=message_id))
        new_comment.save()
    return redirect('/users/show/{}'.format(user_id))

def get_logged_in_user(request):
    try:
        request.session['id']
    except KeyError:
        return None

    return User.objects.get(id=request.session['id'])

def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return redirect('/')

def logged_in(request):
    if not get_logged_in_user(request) == None:
        return True
    else:
        return False

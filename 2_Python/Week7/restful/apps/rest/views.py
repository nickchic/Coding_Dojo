from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
    users = User.objects.all()
    context = {'users': users }
    return render(request, 'rest/users.html', context)

def add_user(request):
    errors = User.objects.user_validate(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/rest/users/new')
    else:
        new_user = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        new_user.save()
        return redirect('/rest')

def edit_user(request):
    errors = User.objects.user_validate(request.POST)
    print len(errors)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/rest/users/{}/edit'.format(request.POST['id']))
    else:
        user_to_edit = User.objects.get(id=request.POST['id'])
        user_to_edit.first_name = request.POST['first_name']
        user_to_edit.last_name = request.POST['last_name']
        user_to_edit.email = request.POST['email']
        user_to_edit.save()
        return redirect('/rest')

def user_page(request, id_num):
    context = {
        'user': User.objects.get(id=id_num)
    }
    return render(request, 'rest/user.html', context)

def new_user_page(request):
    return render(request, 'rest/add_user.html')

def edit_user_page(request, id_num):
    print "edit page"
    user = User.objects.get(id=id_num)
    context = {'user': user }
    return render(request, 'rest/edit_user.html', context)

def destroy_user(request, id_num):
    print "destroy"
    User.objects.get(id=id_num).delete()
    return redirect('/rest')

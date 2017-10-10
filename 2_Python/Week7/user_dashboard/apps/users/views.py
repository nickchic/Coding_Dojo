from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'users/index.html')

def login_page(request):
    return render(request, 'users/login.html')

def login_action(request):
    return HttpResponse('login')

def register_page(request):
    return render(request, 'users/registration.html')

def register_action(request):
    return HttpResponse('reg attempt')

def new_user_page(request):
    return render(request, 'users/new_user.html')

def new_user_action(request):
    return HttpResponse('new user action')

def user_page(request, user_id):
    return render(request, 'users/user_page.html')

def user_dashboard(request):
    return render(request, 'users/dashboard.html')

def admin_dashboard(request):
    return render(request, 'users/dashboard.html')

def edit_user_page(request):
    return render(request, 'users/edit.html')

def edit_admin_page(request, user_id):
    return render(request, 'users/edit.html')

def edit_action(request, user_id):
    return HttpResponse('edit action {}'.format(user_id))

def remove_user(request, user_id):
    return HttpResponse('remove user {}'.format(user_id))

def post_message(request, user_id):
    return HttpResponse('post message {}'.format(user_id))

def post_comment(request, user_id, message_id):
    return HttpResponse('post comment {}, {}'.format(user_id, message_id))

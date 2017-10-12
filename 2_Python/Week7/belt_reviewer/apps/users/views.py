from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Count
from .models import User, Book, Review
import bcrypt

def index(request):
    logged_in_user = get_logged_in_user(request)
    context = {
        'logged_in':logged_in(request)
    }
    return render(request, 'users/index.html', context)

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
        return redirect('/books')
    else:
        return login_fail(request)

def login_fail(request):
    messages.error(request, "Login Failed")
    return redirect('/')


def register_action(request):
    errors = User.objects.user_validation(request.POST)
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
        return redirect('/books')


def user_page(request, user_id):
    try:
        this_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('/')

    reviewed_books = Book.objects.annotate(review_count=Count('reviews')).filter(reviews__reviewer_id=user_id)

    context = {
        'user':this_user,
        'logged_in':logged_in(request),
        'reviewed_books':reviewed_books
    }
    return render(request, 'users/user_page.html', context)

def user_home(request):
    return redirect('/users/{}'.format(get_logged_in_user(request).id))

def main_book_page(request):
    recent_reviews = Review.objects.order_by("-created_at")[:5]
    context = {
        'logged_in':logged_in(request),
        'recent_reviews':recent_reviews,
        'other_books':Book.objects.all()
    }
    return render(request, 'users/book_main.html', context)

def book_page(request, book_id):
    context = {
        'logged_in':logged_in(request),
        'book': Book.objects.get(id=book_id),
    }
    return render(request, 'users/book_main_single.html', context)

def add_review(request, book_id):
    if len(request.POST['content']) > 0:
        new_review = Review(content=request.POST['content'], rating=request.POST['rating'], book_id=book_id, reviewer_id=get_logged_in_user(request).id)
        new_review.save()
    else:
        messages.error(request, 'You left it blank!')
    return redirect('/books/{}'.format(book_id))

def add_page(request):
    if not logged_in:
        return redirect('/')
    authors = Book.objects.values('author').annotate(unique_author=Count('author'))
    context = {
        'books':authors,
        'logged_in':logged_in(request)
    }
    print authors
    return render(request, 'users/add_book.html', context)

def add_review_book(request):

    errors = {}
    author = ''
    if request.POST['author_select'] == 'blank':
        if len(request.POST['author_text']) < 1:
            errors['author'] = "Author can't be blank"
        else:
            author = request.POST['author_text']
    else:
        author = request.POST['author_select']

    if len(request.POST['review_content']) < 1:
        errors['review'] = "Review can't be blank"
    if len(request.POST['book_title']) < 1:
        errors['review'] = "Book title can't be blank"

    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/add')
    else:
        print 'no errors'
        new_book = Book(title=request.POST['book_title'],author=author)
        new_book.save()
        new_review = Review(content=request.POST['review_content'], rating=request.POST['review_rating'], book=new_book, reviewer=get_logged_in_user(request))
        new_review.save()
        return redirect('/books/{}'.format(new_book.id))

    return HttpResponse('add_review_book')

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

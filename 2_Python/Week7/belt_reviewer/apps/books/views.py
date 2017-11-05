# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.db.models import Count
from ..users.views import get_logged_in_user, logged_in
from ..users.models import User
from .models import Book, Review

# Create your views here.
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
    return render(request, 'books/user_page.html', context)

def user_home(request):
    return redirect('/book/users/{}'.format(get_logged_in_user(request).id))

def main_book_page(request):
    recent_reviews = Review.objects.order_by("-created_at")[:5]
    context = {
        'logged_in':logged_in(request),
        'recent_reviews':recent_reviews,
        'other_books':Book.objects.all()
    }
    return render(request, 'books/book_main.html', context)

def book_page(request, book_id):
    context = {
        'logged_in':logged_in(request),
        'book': Book.objects.get(id=book_id),
    }
    return render(request, 'books/book_main_single.html', context)

def add_review(request, book_id):
    if len(request.POST['content']) > 0:
        new_review = Review(content=request.POST['content'], rating=request.POST['rating'], book_id=book_id, reviewer_id=get_logged_in_user(request).id)
        new_review.save()
    else:
        messages.error(request, 'You left it blank!')
    return redirect('/book/{}'.format(book_id))

def add_page(request):
    if not logged_in:
        return redirect('/')
    authors = Book.objects.values('author').annotate(unique_author=Count('author'))
    context = {
        'books':authors,
        'logged_in':logged_in(request)
    }
    print authors
    return render(request, 'books/add_book.html', context)

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
        return redirect('/book/add')
    else:
        print 'no errors'
        new_book = Book(title=request.POST['book_title'],author=author)
        new_book.save()
        new_review = Review(content=request.POST['review_content'], rating=request.POST['review_rating'], book=new_book, reviewer=get_logged_in_user(request))
        new_review.save()
        return redirect('/book/{}'.format(new_book.id))

    return HttpResponse('add_review_book')

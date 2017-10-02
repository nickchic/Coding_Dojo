from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Placeholder to later display all the list of blogs"
    return render(request, 'blogs/index.html')

def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
    	print "*"*50
    	print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = request.POST['name']  # more on session below
    	print "*"*50
    	return redirect("/")
    else:
    	return redirect("/")

def number(request, number):
    response = 'Placeholder to DISPLAY blog {}'.format(number)
    return HttpResponse(response)

def edit(request, number):
    response = 'Placeholder to EDIT blog {}'.format(number)
    return HttpResponse(response)

def delete(request, number):
    print "Delete {}".format(number)
    return redirect(index)

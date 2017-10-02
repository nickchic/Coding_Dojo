from django.shortcuts import render, HttpResponse, redirect

def results(request):
    return render(request, 'survey_app/results.html')

def survey(request):

    return render(request, 'survey_app/survey.html')

def survey_process(request):
    print "form submitted"
    try:
        request.session['times'] += 1
    except KeyError:
        request.session['times'] = 1
    request.session['name'] = request.POST['name']
    request.session['fav_language'] = request.POST['fav_language']
    request.session['location'] = request.POST['location']
    request.session['comment'] = request.POST['comment']
    return redirect('/survey/results')

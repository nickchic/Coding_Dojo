from django.shortcuts import render, HttpResponse
from .models import Lead

def index(request):
    context = {
        'leads':Lead.objects.all()[0:5]
    }
    return render(request, 'pagination/index.html', context)

def search(request, scroll=None):
    name_blank = False
    date_blank = False
    x = int(request.POST['scroll'])-1

    if request.POST['name'] == '':
        name_blank = True

    if request.POST['from'] == '' or request.POST['to'] == '':
        date_blank = True

    if not name_blank and date_blank:
        print 'date blank'
        leads_to_show = Lead.objects.filter(first_name__startswith=request.POST['name'])|Lead.objects.filter(last_name__startswith=request.POST['name'])|Lead.objects.filter(email__startswith=request.POST['name'])
    elif not date_blank and name_blank:
        leads_to_show = Lead.objects.filter(created_at__range=[request.POST['from'], request.POST['to']])
    elif date_blank and name_blank:
        leads_to_show = Lead.objects.all()
    else:
        leads_to_show = Lead.objects.filter(created_at__range=[request.POST['from'], request.POST['to']]).filter(first_name__startswith=request.POST['name'])|Lead.objects.filter(last_name__startswith=request.POST['name'])|Lead.objects.filter(email__startswith=request.POST['name'])

    context = {
        'leads':leads_to_show[x:x+5],
        'count':range(1,(len(leads_to_show)/5)+1)
    }
    return render(request, 'pagination/table.html', context)

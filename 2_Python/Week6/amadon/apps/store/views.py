from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    try:
        request.session['item_sold']
    except KeyError:
        request.session['item_sold'] = {}

    try:
        request.session['money_spent']
    except KeyError:
        request.session['money_spent'] = 0

    return render(request, 'store/index.html');

def success(request):
    return render(request, 'store/success.html');

def purchase(request):
    try:
        request.session['money_spent']
    except KeyError:
        return redirect('/amadon')    


    items_for_sale = [
        {'name':'Gum' , 'price':1.00 },
        {'name':'Book' , 'price':15.00 },
        {'name':'Video Game' , 'price':60.00 },
        {'name':'BluRay' , 'price':24.00 }
    ]
    request.session['item_sold'] = items_for_sale[int(request.POST['item_id']) - 1]


    request.session['amount'] = request.POST['amount']
    request.session['purchase_amount'] = float(request.session['item_sold']['price']) * int(request.POST['amount'])

    request.session['money_spent'] += request.session['purchase_amount']

    print request.session['item_sold']
    return redirect('/amadon/success')

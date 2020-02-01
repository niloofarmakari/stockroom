from django.contrib.auth import logout
from django.shortcuts import render, redirect

from . import models, forms


def logout_view(request):
    logout(request)
    return redirect('/')


def product_manager(request):
    return render(request, 'stockroom/product_manager.html', {
        'products': models.Product.objects.raw('SELECT * FROM stockroom_product'),
    })


def person_manager(request):
    return render(request, 'stockroom/person_manager.html', {
        'persons': models.Person.objects.raw('SELECT * FROM stockroom_person')
    })


def product_view(request, id=None):
    product = models.Product.objects.get(id=id) if id else models.Product()

    if request.POST and request.POST['request'] == 'product':
        form = forms.ProductForm(request.POST, instance=product)
        product = form.save()
        return redirect('/products')

    if request.POST and request.POST['request'] == 'transaction':
        form = forms.TransactionForm(request.POST)
        form.save()
        return redirect(f'/product/{id}')

    if 'deleteTransaction' in request.GET and 'transid' in request.GET:
        transaction = models.Transaction.objects.get(id=request.GET['transid'])
        transaction.delete()
        return redirect(f'/product/{id}')

    if 'deleteProduct' in request.GET and id:
        product.delete()
        return redirect('/products')

    transactions = models.Transaction.objects.filter(product=id)
    return render(request, 'stockroom/product.html', {
        'product': product,
        'count': sum([i.count for i in transactions]),
        'persons': models.Person.objects.all(),
        'transactions': transactions,
    })


def person_view(request, id=None):
    person = models.Person.objects.get(id=id) if id else models.Person()

    if request.POST:
        form = forms.PersonForm(request.POST, instance=person)
        person = form.save()
        return redirect('/persons')

    if 'delete' in request.GET and id:
        person.delete()
        return redirect('/persons')

    return render(request, 'stockroom/person.html', {
        'person': person,
    })

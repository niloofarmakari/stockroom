from django.shortcuts import render
from django.contrib.auth import logout
from django.db.models import Sum
from django.shortcuts import redirect, HttpResponse

from . import models, forms


def logout_view(request):
    logout(request)
    return redirect('/')


def product_manager(request):
    search = []
    search.append(f'(name = "{request.GET["keyword"]}")' if "keyword" in request.GET and request.GET['keyword'] else '')
    # search.append(f'(count > 0)' if 'available' in request.GET else '')
    search.append(f'(product_info = "{request.GET["product_info"]}")' if 'product_info' in request.GET and request.GET['product_info'] else '')

    search = [i for i in search if i]
    query = f'where {" and ".join(search)}' if search else ''

    # transactions = {item['product_id']: item['count'] for item in }
    # products = models.Transaction.objects.select_related().values('name', 'product_info', 'product_id').annotate(count=Sum('count'))
    products = models.Product.objects.raw(f'SELECT * FROM stockroom_product {query}')


    return render(request, 'stockroom/product_manager.html', {
        'products': products,
    })


def provider_manager(request):
    search = []
    search.append(f'(name = "{request.GET["keyword"]}")' if "keyword" in request.GET and request.GET['keyword'] else '')

    search = [i for i in search if i]
    query = f'where {" and ".join(search)}' if search else ''

    return render(request, 'stockroom/provider_manager.html', {
        'providers': models.Person.objects.raw(f'SELECT * FROM stockroom_person {query}')
    })


def product_view(request, id=None):
    product = models.Product.objects.get(id=id) if id else models.Product()

    if request.POST and request.POST['request'] == 'product':
        form = forms.ProductForm(request.POST, instance=product)
        product = form.save()
        return redirect('/products')

    if request.POST and request.POST['request'] == 'transaction':
        print('gaatcha')
        form = forms.TransactionForm(request.POST)
        form.save()
        return redirect(f'/product/{id}')



    if 'delete' in request.GET and id:
        product.delete()
        return redirect('/products')

    transactions = models.Transaction.objects.filter(product=id)
    return render(request, 'stockroom/product.html', {
        'product': product,
        'count': sum([i.count for i in transactions]),
        'providers': models.Person.objects.all(),
        'transactions': transactions,
    })


def provider_view(request, id=None):
    provider = models.Person.objects.get(id=id) if id else models.Person()

    if request.POST:
        form = forms.PersonForm(request.POST, instance=provider)
        provider = form.save()
        return redirect('/providers')

    elif 'delete' in request.GET and id:
        provider.delete()
        return redirect('/providers')

    return render(request, 'stockroom/provider.html', {
        'provider': provider,

        # TODO: get a list of products from this person
        # 'products': models.Product.objects.raw(f'SELECT * FROM stockroom_product where provider_id = {id}') if id else None
    })

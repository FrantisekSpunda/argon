from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from argon.utils import paginateBlocks
from .models import Invoice
from .forms import InvoiceForm, ItemForm
from datetime import date, timedelta
from .utils import searchInvoices
from argon.utils import paginateBlocks


# DASHBOARD ######################
##################################
@login_required(login_url='login')
def frontpage(request):
    return redirect('dashboard')

@login_required(login_url='login')
def dashboard(request):
    profile = request.user.profile

    enddate = date.today()
    startdate = enddate - timedelta(days=30)
    date__range=[startdate, enddate]

    last_5_invoices = profile.invoice_set.all()[:5]
    last_month_invoices = profile.invoice_set.filter(date_exposure__range=date__range)
    invoices = profile.invoice_set.all()

    profit_this_month = 0
    for invoice in last_month_invoices :
        profit_this_month += invoice.total_price
        

    context = {'profile': profile, 'invoices': invoices, 'last_5_invoices': last_5_invoices, 'last_month_invoices': last_month_invoices, 'profit_this_month': profit_this_month}
    return render(request, 'orders/dashboard.html', context)


# INVOICES #######################
##################################
@login_required(login_url='login')
def newInvoice(request):
    # Get number of invoice
    invoices = request.user.profile.invoice_set.all()
    current_date = date.today().strftime("%y%m")
    invoice_id = f'{current_date}{"{:0>4}".format(invoices.count()+1)}'

    # Get form of invoice and item
    invoice = InvoiceForm()
    item = ItemForm()

    if request.method == 'POST':
        invoice = InvoiceForm(request.POST)
        
        if invoice.is_valid():
            invoice = invoice.save(commit=False)
            invoice.invoice_id = invoice_id
            invoice.supplier = request.user.profile
            invoice.save()

            for index in range(len(request.POST.getlist('name'))) :
                item = ItemForm()
                item = item.save(commit=False)
                item.invoice = invoice
                item.name = request.POST.getlist('name')[index]
                item.price = request.POST.getlist('price')[index]
                item.amouth = request.POST.getlist('amouth')[index]
                item.dph = request.POST.getlist('dph')[index]
                item.save()

            invoice.getTotalPrice
            messages.success(request, 'Invoice was succesfully created and sended.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Wrong data in form!')

    context = {'invoice': invoice, 'item': item}
    return render(request, 'orders/invoice-form.html', context)

@login_required(login_url='login')
def invoice(request, pk):
    curr_invoice = request.user.profile.invoice_set.get(id=pk)
    invoice_id = curr_invoice.invoice_id
    invoice = InvoiceForm(instance=curr_invoice)

    curr_items = curr_invoice.item_set.all()
    items = []
    for curr_item in curr_items:
        items.append(ItemForm(instance=curr_item))
        print(curr_item)

    if request.method == 'POST':
        invoice = InvoiceForm(request.POST, instance=curr_invoice)
        if invoice.is_valid():
            invoice = invoice.save(commit=False)
            invoice.invoice_id = invoice_id
            invoice.supplier = request.user.profile
            invoice.save()
            
            curr_invoice.item_set.all().delete()
            for index in range(len(request.POST.getlist('name'))) :
                item = ItemForm()
                item = item.save(commit=False)
                item.invoice = invoice
                item.name = request.POST.getlist('name')[index]
                item.price = request.POST.getlist('price')[index]
                item.amouth = request.POST.getlist('amouth')[index]
                item.dph = request.POST.getlist('dph')[index]
                item.save()

            invoice.getTotalPrice
            messages.success(request, 'Invoice was succesfully updated!')
            return redirect('dashboard')
    print(items)
    context = {'invoice': invoice, 'items': items}
    return render(request, 'orders/invoice-form.html', context)


@login_required(login_url='login')
def invoices(request):
    profile = request.user.profile
    invoices, search_query = searchInvoices(request)

    custom_range, invoices = paginateBlocks(request, invoices, 11)

    context = {'invoices': invoices, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'orders/invoices.html', context)
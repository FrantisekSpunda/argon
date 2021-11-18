from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.conf import settings

from argon.utils import paginateBlocks
from .models import Invoice
from .forms import InvoiceForm, ItemForm, ClientForm
from datetime import date, timedelta, datetime
from .utils import searchArgon
from argon.utils import paginateBlocks

import pdfkit

# DASHBOARD ######################
##################################
@login_required(login_url='login')
def frontpage(request):
    return redirect('dashboard')

@login_required(login_url='login')
def dashboard(request):
    year = date.today().year
    
    profile = request.user.profile

    invoices = profile.invoice_set.all()

    last_5_invoices = profile.invoice_set.all()[:5]

    last_month_invoices = profile.invoice_set.filter(date_exposure__year__gte=year,date_exposure__year__lte=year,date_exposure__month__gte=date.today().month,date_exposure__month__lte=date.today().month)
    
    last_month_clients = profile.client_set.filter(created__year__gte=year,created__year__lte=year,created__month__gte=date.today().month,created__month__lte=date.today().month)
    
    profit_this_month = 0
    for invoice in last_month_invoices :
        profit_this_month += invoice.total_price

    last_year_invoices_count = []
    for month in range(12):
        last_year_invoices_count.append(profile.invoice_set.filter(date_exposure__year__gte=year,date_exposure__year__lte=year,date_exposure__month__gte=month + 1,date_exposure__month__lte=month + 1).count())

    last_year_invoices_sales = []
    for month in range(12):
        month_invoices = profile.invoice_set.filter(date_exposure__year__gte=year,date_exposure__year__lte=year,date_exposure__month__gte=month + 1,date_exposure__month__lte=month + 1)
        month_invoices_sales = 0
        for invoice in month_invoices:
            month_invoices_sales += invoice.total_price
        last_year_invoices_sales.append(month_invoices_sales)
        

    context = {'profile': profile, 'invoices': invoices, 'last_5_invoices': last_5_invoices, 'last_month_invoices': last_month_invoices, 'profit_this_month': profit_this_month, 'last_month_clients': last_month_clients, 'last_year_invoices_count': last_year_invoices_count, 'last_year_invoices_sales': last_year_invoices_sales}
    return render(request, 'orders/dashboard.html', context)


####################
##### INVOICES #####
@login_required(login_url='login')
def newInvoice(request):
    # Get number of invoice
    invoices = request.user.profile.invoice_set.all()
    current_date = date.today().strftime("%y%m")
    invoice_id = f'{current_date}{"{:0>4}".format(invoices.count()+1)}'

    # Get form of invoice and item
    invoice = InvoiceForm()
    var_clients = request.user.profile.client_set.all()
    clients = [(i.id, i.client_name) for i in var_clients]
    invoice.fields['client'] = forms.ChoiceField(choices=clients)
    invoice.fields['client'].widget.attrs.update({'class':'form-control'})
    
    item = ItemForm()

    client = ClientForm()

    if request.method == 'POST':
        if 'submit_invoice' in request.POST:
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
                return redirect('invoices')
            else:
                messages.error(request, 'Wrong data in form!')
        elif 'submit_client' in request.POST:
            client = ClientForm(request.POST)
            if client.is_valid():
                client = client.save(commit=False)
                client.client_owner = request.user.profile
                client.save()

                messages.success(request, 'Client was created.')
                redirect('new-invoice')
            else:
                messages.error(request, 'Client form is not valid!')

    context = {'invoice': invoice, 'item': item, 'client': client}
    return render(request, 'orders/invoice-form.html', context)

@login_required(login_url='login')
def invoice(request, pk):
    curr_invoice = request.user.profile.invoice_set.get(id=pk)
    invoice_id = curr_invoice.invoice_id
    invoice = InvoiceForm(instance=curr_invoice)
    
    var_clients = request.user.profile.client_set.all()
    clients = [(i.id, i.client_name) for i in var_clients]
    invoice.fields['client'] = forms.ChoiceField(choices=clients)
    invoice.fields['client'].widget.attrs.update({'class':'form-control'})

    curr_items = curr_invoice.item_set.all()
    items = []
    for curr_item in curr_items:
        items.append(ItemForm(instance=curr_item))

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
                item.sended = False
                item.save()

            invoice.getTotalPrice
            messages.success(request, 'Invoice was succesfully updated!')
            return redirect('invoices')

    context = {'invoice': invoice, 'items': items}
    return render(request, 'orders/invoice-form.html', context)


@login_required(login_url='login')
def deleteInvoice(request, pk):
    request.user.profile.invoice_set.get(id=pk).delete()
    messages.success(request, 'Invoice was deleted!')
    return redirect('invoices')


@login_required(login_url='login')
def invoices(request):
    if request.method == 'POST':

        invoice = request.user.profile.invoice_set.get(id=request.POST['send_invoce'])
        invoice.sended = True
        invoice.save()

        # send email with invoice
        subject = 'Invoice numb.: '+ invoice.invoice_id +' from '+ invoice.supplier.first_name +' '+ invoice.supplier.last_name
        message = 'Sended invoice from argon web.'
        mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [invoice.client.client_email])

        cookie_list = request.COOKIES
        options = {
                'cookie' : [
                    ('csrftoken', cookie_list['csrftoken']),
                    ('sessionid', cookie_list['sessionid']),
                    ]
                }
        projectUrl = request.get_host() + '/view-invoice/'+ str(invoice.id)

        pdf = pdfkit.from_url(projectUrl,False, options=options)

        mail.attach('invoice-'+invoice.invoice_id, pdf, 'application/pdf')
        mail.send()


    invoices, search_query = searchArgon(request)
    custom_range, invoices = paginateBlocks(request, invoices, 11)

    context = {'invoices': invoices, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'orders/invoices.html', context)


####################
##### CLIENTS #####
@login_required(login_url='login')
def clients(request):

    clients = request.user.profile.client_set.all()
    custom_range, clients = paginateBlocks(request, clients, 11)


    client = ClientForm()
    if request.method == 'POST':
        client = ClientForm(request.POST)
        if client.is_valid():
            client = client.save(commit=False)
            client.client_owner = request.user.profile
            client.save()

            messages.success(request, 'Client was created.')
            redirect('clients')

    context = {'clients': clients, 'client': client, 'custom_range': custom_range}
    return render(request, 'orders/clients.html', context)


@login_required(login_url='login')
def deleteClient(request, pk):
    request.user.profile.client_set.get(id=pk).delete()
    messages.success(request, 'Client was deleted!')
    return redirect('clients')


@login_required(login_url='login')
def newClient(request):
    
    client = ClientForm()

    if request.method == 'POST':
        client = ClientForm(request.POST)
        if client.is_valid():
            client = client.save(commit=False)
            client.client_owner = request.user.profile
            client.save()

            messages.success(request, 'Client was created.')
            return redirect('clients')
        else:
            messages.error(request, 'Client form is not valid!')

    context = {'client': client}


    return render(request, 'orders/client-form.html', context)


@login_required(login_url='login')
def client(request, pk):
    
    curr_client = request.user.profile.client_set.get(id=pk)
    client = ClientForm(instance=curr_client)

    if request.method == 'POST':
        client = ClientForm(request.POST, instance=curr_client)
        if client.is_valid():
            client = client.save(commit=False)
            client.client_owner = request.user.profile
            client.save()

            messages.success(request, 'Client was created.')
            return redirect('clients')
        else:
            messages.error(request, 'Client form is not valid!')

    context = {'client': client}
    return render(request, 'orders/client-form.html', context)


####################
### GENERATE PDF ###

@login_required(login_url='login')
def viewInvoice(request, pk):
    invoice = request.user.profile.invoice_set.get(id=pk)
    items = invoice.item_set.all()
    tax_take = 0
    for item in items:
        tax_take += item.amouth * item.price * item.dph / 100
    total_price_with_tax = tax_take + invoice.total_price

    context = {'invoice': invoice, 'items': items, 'tax_take': tax_take, 'total_price_with_tax': total_price_with_tax}
    return render(request, 'orders/invoice-template.html', context)

def pdfInvoice(request, pk):
    invoice = request.user.profile.invoice_set.get(id=pk)

    cookie_list = request.COOKIES
    # pass the cookies. You can add whatever other options you want to use
    options = {
            'cookie' : [
                ('csrftoken', cookie_list['csrftoken']),
                ('sessionid', cookie_list['sessionid']),
                ]
            }

    # Generate the pdf
    
    projectUrl = request.get_host() + '/view-invoice/'+ str(pk)

    pdf = pdfkit.from_url(projectUrl,False, options=options)

    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="inovice-'+ invoice.invoice_id +'.pdf"'

    return response
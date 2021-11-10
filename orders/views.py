from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Invoice
from .forms import InvoiceForm, ItemForm
from datetime import date


# DASHBOARD ######################
##################################
@login_required(login_url='login')
def frontpage(request):
    return redirect('dashboard')

@login_required(login_url='login')
def dashboard(request):
    profile = request.user.profile

    invoices = profile.invoice_set.all()

    context = {'profile': profile, 'invoices': invoices}
    return render(request, 'orders/dashboard.html', context)


# INVOICES #######################
##################################
@login_required(login_url='login')
def newInvoice(request):
    invoices = request.user.profile.invoice_set.all()
    form = InvoiceForm()
    current_date = date.today().strftime("%y%m")

    form_item = ItemForm()

    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        form_item = ItemForm(request.POST)
        if form.is_valid() and form_item.is_valid():
            invoice = form.save(commit=False)
            invoice.invoice_id = f'{current_date}{"{:0>4}".format(invoices.count()+1)}'
            invoice.supplier = request.user.profile
            invoice.save()

            item = form_item.save(commit=False)

            item.invoice_id = invoice.invoice_id
            item.save()

            messages.success(request, 'Invoice was succesfully created and sended.')
            return redirect('dashboard')

        messages.error(request, 'Wrong data in form!')

    context = {'form': form, 'form_item': form_item}
    return render(request, 'orders/invoice-form.html', context)

@login_required(login_url='login')
def invoice(request, pk):
    invoice = request.user.profile.invoice_set.get(id=pk)
    invoice_id = invoice.invoice_id
    form = InvoiceForm(instance=invoice)

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice_form = form.save(commit=False)
            invoice_form.invoice_id = invoice_id
            invoice_form.supplier = request.user.profile
            invoice_form.save()
            messages.success(request, 'Invoice was succesfully updated!')

            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'orders/invoice-form.html', context)
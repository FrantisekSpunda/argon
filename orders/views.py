from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Invoice
from .forms import InvoiceForm
from datetime import date

@login_required(login_url='login')
def frontpage(request):
    return redirect('dashboard')

@login_required(login_url='login')
def dashboard(request):
    profile = request.user.profile

    invoices = Invoice.objects.all()

    context = {'profile': profile, 'invoices': invoices}
    return render(request, 'orders/dashboard.html', context)


@login_required(login_url='login')
def newInvoice(request):
    invoices = Invoice.objects.all()
    form = InvoiceForm()
    current_date = date.today().strftime("%y%m")

    if request.method == 'POST':

        form = InvoiceForm(request.POST)
        invoice = form.save(commit=False)
        invoice.invoice_id = f'{current_date}{"{:0>4}".format(invoices.count()+1)}'
        invoice.supplier = request.user.profile
        invoice.save()

        messages.success(request, 'Invoice was succesfully created and sended.')
        return redirect('dashboard')

    context = {'form': form}
    return render(request, 'orders/new-invoice.html', context)
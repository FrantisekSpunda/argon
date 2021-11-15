from django.db.models import Q

# Search functionality for invoices
def searchInvoices(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    invoices = request.user.profile.invoice_set.distinct().filter(
        Q(invoice_id__icontains=search_query)
    )
    return invoices, search_query

def searchClients(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    clients = request.user.profile.client_set.distinct().filter(
        Q(client_name__icontains=search_query)
    )
    return clients, search_query
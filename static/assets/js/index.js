const invoiceItems_button = document.querySelector('#invoice_items-button')

invoiceItems_button.addEventListener('click', () => {
    const invoiceItems_form = document.querySelector('.invoice_items-form').cloneNode(true)
    const invoiceItems_body = document.querySelector('#invoice_items-body')

    invoiceItems_body.appendChild(invoiceItems_form)
})
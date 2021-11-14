// Adding itemForm in invoiceForm

const invoiceItems_new = document.querySelector('#invoice_items-new')
const invoiceItems_close = document.querySelectorAll('.invoice_items-close')
console.log(invoiceItems_close);
const invoiceItems_body = document.querySelector('#invoice_items-body')

const createItemForm = (() => {
    const invoiceItems_form = document.createElement('tr')
    invoiceItems_form.classList.add('invoice_items-form')
    invoiceItems_form.innerHTML = `<th scope="row">
                                        <input type="text" name="name" maxlength="128" class="form-control" placeholder="name" id="id_name">
                                    </th>
                                    <td>
                                        <input type="number" name="price" value="0" step="any" class="form-control" placeholder="price" id="id_price">
                                    </td>
                                    <td>
                                        <input type="number" name="amouth" value="1" class="form-control" placeholder="amouth" id="id_amouth">
                                    </td>
                                    <td>
                                        <input type="number" name="dph" value="21" step="any" class="form-control" placeholder="dph" id="id_dph">
                                    </td>
                                    <td></td>`

    const invoiceItems_close = document.createElement('button')
    let classesToAdd = ['invoice_items-close', 'btn', 'btn-outline-primary', 'rounded-circle', 'btn-sm']
    classesToAdd.forEach(classToAdd => {
        invoiceItems_close.classList.add(classToAdd)
    });
    invoiceItems_close.setAttribute('type', 'button')
    invoiceItems_close.innerHTML = '<span class="btn-inner--icon"><i class="ni ni-fat-remove"></i></span>'
    invoiceItems_close.addEventListener('click', () => {
        invoiceItems_body.removeChild(invoiceItems_form)
    })

    const formTds = invoiceItems_form.getElementsByTagName('td')
    formTds[formTds.length - 1].appendChild(invoiceItems_close)

    return invoiceItems_form
})

invoiceItems_new.addEventListener('click', () => {
    invoiceItems_body.appendChild(createItemForm())
})

invoiceItems_close.forEach(closeButton => {
    closeButton.addEventListener('click', () => {
        invoiceItems_body.removeChild(closeButton.parentElement.parentElement)
    })
});
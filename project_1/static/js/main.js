import { addToCart, clearCart, renderCart, cartItemCount, showItemCart } from './cart.js'

const cartOpen = document.getElementById('cart-open')
const cartBody = document.getElementById('modal-body')
const addProduct = document.getElementById('product-add')
const cartClearBtn = document.getElementById('cart-clear-btn')
const cartCount = document.getElementById('cart-count')


if (addProduct) {
    addProduct.addEventListener('click', (e) => {
        addToCart(e, '.page-product__title', '.page-product__price', addProduct, cartCount)
    })
    showItemCart(addProduct)
}
cartClearBtn.addEventListener('click', () => clearCart(cartBody, addProduct, cartCount))
cartOpen.addEventListener('click', () => renderCart(cartBody, cartCount, addProduct))
cartItemCount(cartCount)
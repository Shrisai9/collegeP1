// cart.js

// Get the cart icon and total span elements
const cartIcon = document.querySelector('.fa-shopping-cart');
const totalSpan = document.getElementById('total');

// Function to add an item to the cart
function addItemToCart(button) {
  const productData = button.parentElement.dataset.product.split(',');
  const product = productData[0];
  const price = parseFloat(productData[1]);

  // Check if the item is already in the cart
  const existingItem = cartItems.find((item) => item.product === product);
  if (existingItem) {
    // If the item is already in the cart, increment its quantity
    existingItem.quantity++;
  } else {
    // If the item is not in the cart, add it with a quantity of 1
    cartItems.push({ product, price, quantity: 1 });
  }

  // Update the cart icon and total span
  updateCartIconAndTotal();
}

// Function to remove an item from the cart
function removeItemFromCart(productData) {
  // Find the item in the cart items array
  const itemIndex = cartItems.findIndex((item) => item.product === productData.product);
  if (itemIndex!== -1) {
    // Remove the item from the cart items array
    cartItems.splice(itemIndex, 1);
  }

  // Update the cart icon and total span
  updateCartIconAndTotal();
}

// Function to update the cart icon and total span
function updateCartIconAndTotal() {
  // Calculate the total price of the items in the cart
  let total = 0;
  cartItems.forEach((item) => {
    total += item.price * item.quantity;
  });

  // Update the cart icon and total span
  cartIcon.dataset.total = total.toFixed(2);
  totalSpan.textContent = total.toFixed(2);

  // Render the cart items in the cart page
  const cartItemsElement = document.getElementById('cart-items');
  cartItemsElement.innerHTML = '';
  cartItems.forEach((item) => {
    const cartItemElement = document.createElement('li');
    cartItemElement.textContent = `${item.product} - $${item.price} x ${item.quantity}`;
    cartItemsElement.appendChild(cartItemElement);
  });
}
// Initialize the cart items array
let cartItems = [];

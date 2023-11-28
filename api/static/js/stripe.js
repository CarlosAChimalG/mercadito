// static/tu_script_de_stripe.js

var stripe = Stripe('pk_test_51OCU7RDU5FTAbIUafQkvL9dK8piJ8KGMzYL66TcgbAEExt56cPDiOK1iwFRt3Ni2qYPSaQp2DCDLsp2RtSzyll0000UnP6YAX9');
var elements = stripe.elements();

// Create an instance of the card Element.
var card = elements.create('card');

// Add an instance of the card Element into the `card-element` div.
card.mount('#card-element');

// Handle real-time validation errors from the card Element.
card.addEventListener('change', function(event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
});

// Handle form submission.
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
  event.preventDefault();

  stripe.createToken(card).then(function(result) {
    if (result.error) {
      var errorElement = document.getElementById('card-errors');
      errorElement.textContent = result.error.message;
    } else {
      // Actualiza el valor del campo stripeToken antes de enviar el formulario
      document.getElementById('stripeToken').value = result.token.id;
      // Envía el formulario
      form.submit();
    }
  });
});


// Submit the form with the token ID.
function stripeTokenHandler(token) {
  // Insert the token ID into the form so it gets submitted to the server.
  var form = document.getElementById('payment-form');
  var hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripeToken');
  hiddenInput.setAttribute('value', token.id);
  form.appendChild(hiddenInput);

  // Submit the form.
  form.submit();
}

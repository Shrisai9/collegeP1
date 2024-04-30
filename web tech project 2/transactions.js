document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const flowerCheckboxes = document.querySelectorAll('input[name="flowers[]"]');
  const deliveryOptions = document.querySelectorAll('input[name="delivery"]');

  // Function to check if at least one flower is selected
  function isAnyFlowerSelected() {
    return Array.from(flowerCheckboxes).some((checkbox) => checkbox.checked);
  }

  // Function to check if a delivery method is selected
  function isDeliveryMethodSelected() {
    return Array.from(deliveryOptions).some((radio) => radio.checked);
  }

  // Form submission handler
  form.addEventListener("submit", function (e) {
    if (!isAnyFlowerSelected()) {
      e.preventDefault(); // Prevent form from submitting
      alert("Please select at least one flower.");
    } else if (!isDeliveryMethodSelected()) {
      e.preventDefault();
      alert("Please select a delivery method.");
    }
  });
});

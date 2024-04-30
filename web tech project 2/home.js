// JavaScript to handle modal display
function showModal(flowerName, flowerPrice) {
  // Get the modal elements
  const modal = document.getElementById("flowerModal");
  const modalContent = document.getElementById("modalContent");
  const modalText = document.getElementById("modalText");

  // Set the modal text with flower details
  modalText.innerText = `Flower: ${flowerName}\nPrice: ${flowerPrice}`;

  // Display the modal
  modal.style.display = "block";
}

function closeModal() {
  // Close the modal
  const modal = document.getElementById("flowerModal");
  modal.style.display = "none";
}

// Add click events to flower cards to show modal
document.addEventListener("DOMContentLoaded", () => {
  const flowerCards = document.querySelectorAll(".flower-card");

  flowerCards.forEach((card) => {
    const flowerName = card.querySelector("h3").innerText;
    const flowerPrice = card.querySelector("p").innerText;

    card.addEventListener("click", () => {
      showModal(flowerName, flowerPrice);
    });
  });

  // Set close modal on clicking outside the modal content
  const modal = document.getElementById("flowerModal");
  modal.addEventListener("click", (event) => {
    if (event.target === modal) {
      closeModal();
    }
  });
});

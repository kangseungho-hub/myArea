function accountModalToggleHandler(targetSelector) {

    var targetModal = document.querySelector(targetSelector)
    var allModal = document.querySelectorAll(".account-modal-container")

    allModal.forEach(function(modal) { modal.style.display = "none" })
    targetModal.style.display = "block"
}
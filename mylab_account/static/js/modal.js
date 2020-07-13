function modalToggleHandler(targetSelector) {

    var targetModal = document.querySelector(targetSelector)


    targetModal.style.display = "block"
}

function modalCloseHandler(targetSelector) {
    var targetModal = document.querySelector(targetSelector)

    targetModal.style.display = "None"

}
$(".findaccount-form").submit((e) => {
    var target = document.querySelector(".findaccount-btn")
    var loading = `<div class="loader"></div>`
    var original = target.innerHTML
    target.innerHTML = loading

    findAccuntError.innerText = ""
    all_complete = true

    $.ajax({
        type: "GET",
        url: emailExistCheckURL,
        data: { "email": findAccountEmailInput.value },
        dataType: "json",
        async: false,
        success: function(resp) {
            if (!resp.emailExist) {
                all_complete = false
                findAccuntError.style.color = "red"
                findAccuntError.innerText = "this email not registerd in server"
            }
        }
    })

    target.innerHTML = original

    return all_complete
})
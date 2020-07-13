const CSRF_TOKEN = getCookie("csrftoken")

$(".login-form").submit((e) => {
    var target = document.querySelector(".login-btn")
    var loading = `<div class="loader"></div>`
    var original = target.innerHTML
    target.innerHTML = loading

    loginError.innerText = ""
    var all_complete = true
    $.ajax({
        type: "POST",
        url: accountExistCheckURL,
        data: {
            "username": loginUsernameInput.value,
            "password": loginPasswordInput.value,
            "csrfmiddlewaretoken": getCookie("csrftoken"),
        },
        dataType: "json",
        async: false,
        success: function(resp) {
            console.log(resp)
            if (!resp.accountExist) {
                all_complete = false
                loginError.style.color = "red"
                loginError.innerText = "this account not registered in server"
            }
        }
    })
    target.innerHTML = original

    return all_complete
})
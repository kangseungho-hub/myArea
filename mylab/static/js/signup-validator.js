//jquery를 사용하면 false가 return될 경우 submission이 진행되지 않음
// vanila js는 onsubmit인가 form태그에  옵션으로 넣으면  됨
//근데 하여튼 jquery는 안그래도 됨
$(".signup-form").submit((e) => {
    var target = document.querySelector(".signup-btn")
    var loading = `<div class="loader"></div>`
    var original = target.innerHTML
    target.innerHTML = loading


    var all_complete = true


    var validator = { username: validateUserName, email: validateEmail, password: passwordValidate }

    for (var validate in validator) {
        console.log(validate)
        if (true != validator[validate]()) {
            all_complete = false
        }
    }

    $.ajax({
        type: "GET",
        url: usernameExistCheckURL,
        data: {
            "username": usernameInput.value,
        },
        async: false,
        dataType: "json",
        success: function(resp) {
            if (resp.usernameExist) {
                usernameError.style.color = "red"
                usernameError.innerText = "this username is already useing"
                all_complete = false
                console.log("username checked!")
                console.log(resp)
            }
        }
    })

    $.ajax({
        type: "GET",
        url: emailExistCheckURL,
        data: {
            'email': emailInput.value,
            // 'csrfmiddlewaretoken': csrf_token,
        },
        async: false,
        dataType: "json",
        success: function(resp) {
            if (resp.emailExist) {
                emailError.style.color = "red"
                emailError.innerText = "your email already has account"

                all_complete = false
                console.log("email checked!")
                console.log(resp)
            }
        }
    })

    target.innerHTML = original
    return all_complete
})




function validateUserName() {
    var username = usernameInput.value


    if (username.length > 15 || username.length < 3) {
        usernameError.style.color = "red"
        usernameError.innerText = "username : must shorter than 15character and longer than 3chracter"
        return false
    }

    return true
}

function validateEmail() {
    var email = emailInput.value

    if (!email_re.test(email)) {
        emailError.style.color = "red"
        emailError.innerText = "Email : unvalid format"
        return false
    }

    return true
}



function passwordValidate() {
    var p1 = password1Input.value
    var p2 = password2Input.value

    if (p1.length > 20 || p1.length < 10) {
        passwordError.style.color = "red"
        passwordError.innerText = "password : must shorter than 30 character and longer than 10 character"
        return false
    }

    if (p1 != p2) {
        passwordError.style.color = "red"
        passwordError.innerText = "password is not corrected"
        return false
    }
    return true
}
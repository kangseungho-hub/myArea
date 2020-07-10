const usernameInput = document.querySelector(".username-input")
const usernameError = document.querySelector(".username-error-text")

const emailInput = document.querySelector(".email-input")
const emailError = document.querySelector(".email-error-text")

const password1Input = document.querySelector(".pw1-input")
const password2Input = document.querySelector(".pw2-input")
const passwordError = document.querySelector(".password-error-text")

const email_re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;


const validate_pass = { username: false, email: false, password: false, password_correct: false }



//이거 그냥 다 제출했을 떄로 변경해라 시1발 죽기싫으면

usernameInput.addEventListener("input", (e) => {
    check_validate()
    var username = e.target.value

    usernameError.style.color = "green"
    usernameError.innerText = "username : good"


    if (username.length > 15 || username.length < 3) {
        usernameError.style.color = "red"
        usernameError.innerText = "username : must shorter than 15character and longer than 3chracter"
        validate_pass.username = false
        return 0
    }
    validate_pass.username = true
})


emailInput.addEventListener("input", (e) => {
    check_validate()
    var email = e.target.value

    emailError.style.color = "green"
    emailError.innerText = "Email : good!"

    if (!email_re.test(email)) {
        emailError.style.color = "red"
        emailError.innerText = "Email : unvalid format"
        validate_pass.email = false
        return 0
    }
    validate_pass.email = true
})


password1Input.addEventListener("input", (e) => {
    check_validate()
    var password = e.target.value

    passwordError.style.color = "green"
    passwordError.innerText = "password : good"

    if (password.length > 20 || password.length < 10) {
        passwordError.style.color = "red"
        passwordError.innerText = "password : must shorter than 20 character and longer than 10 character"
        validate_pass.password = false
        return 0
    }
    validate_pass.password = true
})

password2Input.addEventListener("input", (e) => {
    check_validate()
    var password1 = password1Input.value
    var password2 = e.target.value

    passwordError.style.color = "green"
    passwordError.innerText = "password : good"
    if (password1 != password2) {
        passwordError.style.color = "red"
        passwordError.innerText = "password is not corrected"
        validate_pass.password_correct = false
        return 0
    }
    validate_pass.password_correct = true
})



function check_validate() {
    for (const validate in validate_pass) {
        if (validate_pass[validate] != true) {
            document.querySelector(".signup-btn").style.display = "none"
            return 0
        }
    }
    console.log("all passed!")
    document.querySelector(".signup-btn").style.display = "block"
}
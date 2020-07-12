//use for signup validation
const signup_form = document.querySelector(".signup-form")
const usernameInput = document.querySelector(".username-input")
const usernameError = document.querySelector(".username-error-text")

const emailInput = document.querySelector(".email-input")
const emailError = document.querySelector(".email-error-text")
const email_re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

const password1Input = document.querySelector(".pw1-input")
const password2Input = document.querySelector(".pw2-input")
const passwordError = document.querySelector(".password-error-text")




//use for login validation
const login_form = document.querySelector(".login-form")
const loginUsernameInput = document.querySelector(".login-username")
const loginPasswordInput = document.querySelector(".login-password")


//use for find-account validation
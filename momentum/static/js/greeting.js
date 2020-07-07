const form = document.querySelector(".js-form"),
    input = document.querySelector("input"),
    greeting = document.querySelector(".js-greetings");


const USER_LS = "currentUser",
    SHOWING_ON = "showing";

function saveName(name) {
    localStorage.setItem(USER_LS, name)
}

function handleSubmit(e) {
    e.preventDefault();
    const currentValue = input.value;
    paintGreeting(currentValue)
    saveName(currentValue)
}

function askForName() {
    form.classList.add(SHOWING_ON)
    form.addEventListener("submit", handleSubmit)
}

function paintGreeting(text) {
    form.classList.remove(SHOWING_ON)
    greeting.classList.add(SHOWING_ON)
    greeting.innerText = `- ${text} - `
}

function loadName() {
    const currentUser = localStorage.getItem(USER_LS)
    if (currentUser === null) {
        askForName()
    } else {
        paintGreeting(currentUser)
    }
}


function init() {
    loadName()
}

init()
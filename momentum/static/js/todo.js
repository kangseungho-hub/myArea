const toDoForm = document.querySelector(".js-toDoForm"),
    toDoInput = toDoForm.querySelector("input"),
    toDoList = document.querySelector(".js-toDoList");

const TODOS_LS = "toDos"

let toDos = []


function deleteToDo(event) {
    const btn = event.target
    const li = btn.parentNode;
    toDoList.removeChild(li)
    const cleanToDos = toDos.filter(function(toDo) {
        return toDo.id !== parseInt(li.id);
    })

    toDos = cleanToDos;
    saveToDos()

}

function crossLineToDO(event) {
    const btn = event.target;
    const toDoText = btn.previousSibling

    toDoText.classList.add("crossLine")

}

function delCrossLineToDo(event) {
    const btn = event.target;
    const toDoText = btn.previousSibling

    toDoText.classList.remove("crossLine")
}

function saveToDos() {
    localStorage.setItem(TODOS_LS, JSON.stringify(toDos))
}

function handleSubmit(event) {
    event.preventDefault();
    const currentValue = toDoInput.value;
    toDoInput.value = ""
    paintToDo(currentValue)
}

function paintToDo(text) {
    const li = document.createElement("li")
    const delBtn = document.createElement("button")


    delBtn.innerText = "X"
    delBtn.classList.add("deleteToDo")

    delBtn.addEventListener("click", deleteToDo)
    delBtn.addEventListener("mouseover", crossLineToDO)
    delBtn.addEventListener("mouseleave", delCrossLineToDo)
    const span = document.createElement("span")
    span.classList.add("toDoText")
    const newId = toDos.length + 1;
    span.innerText = text
    li.appendChild(span);
    li.appendChild(delBtn);
    li.id = newId
    delBtn.id = newId;
    li.classList.add("toDo")
    toDoList.appendChild(li)

    const toDoObj = {
        text: text,
        id: newId,
    }

    toDos.push(toDoObj)
    saveToDos()
}

function loadToDos() {
    const loadedToDos = localStorage.getItem(TODOS_LS);
    if (loadedToDos !== null) {
        const parseToDos = JSON.parse(loadedToDos)

        parseToDos.forEach(function(toDo) {
            paintToDo(toDo.text)
        })
    }
}


function init() {
    loadToDos();
    toDoForm.addEventListener("submit", handleSubmit)
}





init();
const API_KEY = "8c472187aa4d013e97f575d12933424b"
    //https://home.openweathermap.org/


const COORDS = 'coords'

const weather = document.querySelector('.js-country-info')



function saveCoords(coordsObj) {
    localStorage.setItem(COORDS, JSON.stringify(coordsObj))
}

function getCurrentWeather(lat, lon) {
    getCW_url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
    fetch(getCW_url).then(function(response) {
        return response.json()
    }).then(function(json) {
        console.log(json)
        const Temperture = json.main.temp;
        const Country = json.sys.country;
        const place = json.name

        weather.innerText = `@${Country}(${place})  temperture : ${Temperture} `

    })


}

function handleGeoSuccess(position) {
    const latitude = position.coords.latitude
    const longitude = position.coords.longitude
    console.log(position)
    const coordsObj = {
        latitude,
        longitude,
    }

    saveCoords(coordsObj)
    getCurrentWeather(latitude, longitude)
}

function handleGeoError() {
    console.log("Cant access geo location ")
}

function askForCoords() {
    navigator.geolocation.getCurrentPosition(handleGeoSuccess, handleGeoError)
}

function loadCoords() {
    const loadedCoords = localStorage.getItem(COORDS)
    if (loadedCoords === null) {
        askForCoords();
    } else {
        const parseCoords = JSON.parse(loadedCoords)
        getCurrentWeather(parseCoords.latitude, parseCoords.longitude)
    }
}

function init() {
    loadCoords();

}

init();
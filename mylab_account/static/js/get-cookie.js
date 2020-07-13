function getCookie(cookieName) {
    var cookiesArray = document.cookie.split(";")

    for (cookie in cookiesArray) {
        var keyValue = cookiesArray[cookie].split("=")
        if (keyValue[0] == cookieName) {
            return keyValue[1]
        }
    }

    return false
}
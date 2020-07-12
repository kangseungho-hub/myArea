$.(".login-form").submit((e) => {
    all_complete = true
    $.ajax({
        type: "POST",
        url: accountExistCheck,
        data: {
            "username": loginUsernameInput,
            "password": loginPasswordInput,
        },
        async: false;
        dataType: "json",
        success: function(resp) {
            if (resp.accountExist) {
                all_complete = false
            }
        }
    })

    return all_complete
})
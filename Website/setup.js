function Save() {
    eel.SaveLogin(document.getElementById("username").value, document.getElementById("password").value, document.getElementById("lastname").value, document.getElementById("firstname").value); 
    eel.SetLoggedInFalse()
    window.location = "home.html"
}

function Setup() {
    eel.SetupSetup()
}
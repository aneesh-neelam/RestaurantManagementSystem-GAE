/**
 * Created by 'Aneesh Neelam <neelam.aneesh@gmail.com>' on 21/4/14.
 */

function validateForm() {
    var name = document.forms["RegistrationForm"]["name"].value;
    var email = document.forms["RegistrationForm"]["email"].value;
    var passwd = document.forms["RegistrationForm"]["password"].value;
    var cpasswd = document.forms["RegistrationForm"]["confirmPassword"].value;
    var buttonElt = document.getElementById("submit");
    if (name.length == 0 || email.length == 0 || passwd.length == 0 || cpasswd.length == 0) {
        buttonElt.className = "button disabled";
    }
    else if (validateName(name) && validateEmail(email) && validatePassword(passwd, cpasswd)) {
        buttonElt.className = "button";
    }
    else {
        buttonElt.className = "button";
    }
}

function validateName(name) {
    var NameErrorElt = document.getElementById("NameError");
    var nameRegEx = new RegExp("\\w");
    if (nameRegEx.test(name)) {
        NameErrorElt.style.visibility = "collapse";
        return true;
    }
    else {
        NameErrorElt.style.visibility = "visible";
        return false;
    }
}

function validateEmail(email) {
    var emailErrorElt = document.getElementById("EmailError");
    var atpos = email.indexOf("@");
    var dotpos = email.lastIndexOf(".");
    if (atpos < 1 || dotpos < atpos + 2 || dotpos + 2 >= email.length) {
        emailErrorElt.style.visibility = "visible";
        return false;
    }
    else {
        emailErrorElt.style.visibility = "collapse";
        return true;
    }
}


function validatePassword(passwd, cpasswd) {
    var passwordErrorElt = document.getElementById("PasswordError");
    if (passwd == cpasswd) {
        passwordErrorElt.style.visibility = "collapse";
        return true;
    }
    else {
        passwordErrorElt.style.visibility = "visible";
        return false;
    }
}
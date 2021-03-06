/**
 * Created by 'Aneesh Neelam <neelam.aneesh@gmail.com>' on 26/4/14.
 */

function validateForm() {
    var fname = document.forms["RegistrationForm"]["fname"].value;
    var lname = document.forms["RegistrationForm"]["lname"].value;
    var email = document.forms["RegistrationForm"]["email"].value;
    var phone = document.forms["RegistrationForm"]["password"].value;
    var passwd = document.forms["RegistrationForm"]["password"].value;
    var cpasswd = document.forms["RegistrationForm"]["confirmPassword"].value;
    var buttonElt = document.getElementById("submit");
    if (fname.length == 0 || lname.length == 0 || email.length == 0 || phone.length == 0 || passwd.length == 0 || cpasswd.length == 0) {
        buttonElt.className = "button disabled";
    }
    else if (validateName(fname, lname) && validateEmail(email) && validatePhone(phone) && validatePassword(passwd, cpasswd)) {
        buttonElt.className = "button";
    }
}

function validateName(fname, lname) {
    var NameErrorElt = document.getElementById("NameError");
    var nameRegEx = new RegExp("[A-Za-z]");
    if (nameRegEx.test(fname) && nameRegEx.test(lname)) {
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

function validatePhone(phone) {

    var phoneErrorElt = document.getElementById("PhoneError");
    var phoneRegEx = new RegExp("[0-9]");
    if (phoneRegEx.test(phone)) {
        phoneErrorElt.style.visibility = "collapse";
        return true;
    }
    else {
        phoneErrorElt.style.visibility = "visible";
        return false;
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
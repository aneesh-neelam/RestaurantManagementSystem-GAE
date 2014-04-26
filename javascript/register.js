/**
 * Created by 'Aneesh Neelam <neelam.aneesh@gmail.com>' on 21/4/14.
 */

function validatePassword() {
    var p1 = document.forms["registrationForm"]["password"].value;
    var p2 = document.forms["registrationForm"]["confirmPassword"].value;
    var errorElement = document.getElementById("PasswordError");
    if (p1.length == 0 && p2.length == 0) {
        errorElement.style.visibility = "collapse";
    }
    else if (p1 != p2) {
        errorElement.style.visibility = "visible";
    }
    else if (p1 == p2) {
        errorElement.style.visibility = "collapse";
    }
}
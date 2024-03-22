// validation.js

// Function to hide message after 2 seconds of inactivity
function hideMessageAfterInactivity() {
    setTimeout(function () {
        var messageDiv = document.querySelector('.log_message');
        var messageDiv1 = document.querySelector('.sign_message');
        if (messageDiv) {
            // Hide the message
            messageDiv.style.display = 'none';
            messageDiv1.style.display = 'none';
        }
    }, 2000); // Hide after 2 seconds (2000 milliseconds)
}

// Call the hideMessageAfterInactivity function when the page loads
window.onload = function () {
    hideMessageAfterInactivity();

    // Add event listener to the document to reset the timer when clicking anywhere
    document.addEventListener('click', function () {
        var messageDiv = document.querySelector('.log_message');
        var messageDiv1 = document.querySelector('.sign_message');

        if (messageDiv && messageDiv1) {
            // Show the message
            // messageDiv.style.display = 'block';

            // Reset the timeout
            clearTimeout(timeout);

            // Set the timeout again
            // hideMessageAfterInactivity();
        }
    });
};



// Function to validate login form
function validateLoginForm() {
    // Get the username and password fields
    var username = document.querySelector('.login-form input[name="username"]').value;
    var password = document.querySelector('.login-form input[name="password"]').value;
    // Basic validation - check if username and password are not empty
    if (username.trim() === '' || password.trim() === '') {
        alert('Please enter your username and password.');
        return false;
    }

    return true;
}







// / Function to validate registration form
function validateRegistrationForm() {
    // Get all the input fields from the registration form
    var username = document.querySelector('.signup-form input[name="username"]').value;
    var email = document.querySelector('.signup-form input[name="email"]').value;
    var password = document.querySelector('.signup-form input[name="password"]').value;
    var address = document.querySelector('.signup-form input[name="address"]').value;
    var phone = document.querySelector('.signup-form input[name="phone"]').value;

    // Basic validation - check if any field is empty
    if (username.trim() === '' || email.trim() === '' || password.trim() === '' || address.trim() === '' || phone.trim() === '') {
        alert('Please fill in all fields for registration.');
        return false;
    }

    // If all fields are filled, registration is successful
    showRegistrationSuccess();
    return true;
}

// Function to show registration success message
function showRegistrationSuccess() {
    // You can customize this function to display a message to the user
    alert('Registration successful! Thank you for signing up.');
}







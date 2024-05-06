document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;

    // Perform your login logic here, e.g. sending a request to the server.
    console.log(`Logging in with email: ${email}`);
});
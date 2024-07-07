const loginForm = document.getElementById('login-form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const errorMessage = document.getElementById('error-message');

loginForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission behavior

  // Reset any previous error messages
  errorMessage.textContent = '';

  // Basic validation
  let isValid = true;
  if (emailInput.value === '') {
    errorMessage.textContent = 'Please enter your email or phone number.';
    isValid = false;
  } else if (!validateEmail(emailInput.value) && !validatePhone(emailInput.value)) {
    errorMessage.textContent = 'Invalid email or phone format.';
    isValid = false;
  }
  if (passwordInput.value === '') {
    errorMessage.textContent = 'Please enter your password.';
    isValid = false;
  }

  // Submit the form only if validation is successful
  if (isValid) {
    loginForm.submit();
  }
});

function validateEmail(email) {
  const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

function validatePhone(phone) {
  // phone number validation
  const re = /^\d{10}$/;
  return re.test(phone);
}

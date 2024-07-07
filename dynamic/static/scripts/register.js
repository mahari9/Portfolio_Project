const registerForm = document.getElementById('register-form');
const emailInput = document.getElementById('email');
const phoneInput = document.getElementById('phone');
const fullNameInput = document.getElementById('full_name');
const password1Input = document.getElementById('password1');
const password2Input = document.getElementById('password2');
const errorMessage = document.getElementById('error-message');

registerForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission behavior

  // Reset any previous error messages
  errorMessage.textContent = '';

  // Basic validation
  let isValid = true;
  if (emailInput.value === '') {
    errorMessage.textContent = 'Please enter your email address.';
    isValid = false;
  } else if (!validateEmail(emailInput.value)) {
    errorMessage.textContent = 'Invalid email format.';
    isValid = false;
  }
  if (fullNameInput.value === '') {
    errorMessage.textContent = 'Please enter your full name.';
    isValid = false;
  } else if (fullNameInput.value.length < 5) {
    errorMessage.textContent = 'Full name must be at least 5 characters long.';
    isValid = false;
  }
  if (password1Input.value === '') {
    errorMessage.textContent = 'Please enter a password.';
    isValid = false;
  } else if (password1Input.value.length < 4) {
    errorMessage.textContent = 'Password must be at least 4 characters long.';
    isValid = false;
  }
  if (password2Input.value === '') {
    errorMessage.textContent = 'Please confirm your password.';
    isValid = false;
  } else if (password1Input.value !== password2Input.value) {
    errorMessage.textContent = 'Passwords do not match.';
    isValid = false;
  }
  // Optional validation for phone number (adjust based on your needs)
  if (phoneInput.value !== '') {
    if (phoneInput.value.length !== 10 && phoneInput.value.length !== 15) {
      errorMessage.textContent = 'Invalid phone number format.';
      isValid = false;
    }
  }
   // Submit the form only if validation is successful
  if (isValid) {
    registerForm.submit();
  }
});

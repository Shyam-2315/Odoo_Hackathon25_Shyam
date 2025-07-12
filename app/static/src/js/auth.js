function initAuthForms() {
    // Login Form
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('[name="email"]').value;
            const password = this.querySelector('[name="password"]').value;
            
            // Basic validation
            if (!email || !password) {
                showError(this, 'Please fill in all fields');
                return;
            }
            
            console.log('Login attempt:', { email, password });
            // AJAX login call would go here
        });
    }
    
    // Registration Form
    const registerForm = document.getElementById('register-form');
    if (registerForm) {
        registerForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('[name="email"]').value;
            const password = this.querySelector('[name="password"]').value;
            const confirmPassword = this.querySelector('[name="confirm_password"]').value;
            
            // Validation
            if (password !== confirmPassword) {
                showError(this, 'Passwords do not match');
                return;
            }
            
            console.log('Registration attempt:', { email, password });
            // AJAX registration call would go here
        });
    }
}

function showError(form, message) {
    const errorElement = form.querySelector('.form-error');
    if (errorElement) {
        errorElement.textContent = message;
        errorElement.style.display = 'block';
    }
}
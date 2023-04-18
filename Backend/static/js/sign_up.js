function comparePasswords() {
    const password = document.getElementById('password');
    const confirmUsernameInput = document.getElementById('confirm_password');
    const submitBtn = document.getElementById('boton');
    
    confirmUsernameInput.addEventListener('input', () => {
        if (password.value === confirmUsernameInput.value) {
            submitBtn.textContent = "Enviar"
            submitBtn.disabled = false;
        } else {
            submitBtn.textContent = "Las contraseñas no coinciden."
            submitBtn.disabled = true;
        }
    });
}
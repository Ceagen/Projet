document.addEventListener('DOMContentLoaded', () => {
    const userIcon = document.getElementById('userIcon');
    const loginOverlay = document.getElementById('loginOverlay');
    const closeLogin = document.getElementById('closeLogin');

    userIcon.addEventListener('click', () => {
        loginOverlay.style.display = 'flex';
    });

    closeLogin.addEventListener('click', () => {
        loginOverlay.style.display = 'none';
    });

    // Optional: close if clicking outside form
    loginOverlay.addEventListener('click', (e) => {
        if (e.target === loginOverlay) {
            loginOverlay.style.display = 'none';
        }
    });
})
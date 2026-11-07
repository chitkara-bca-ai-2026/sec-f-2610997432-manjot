document.addEventListener('DOMContentLoaded', () => {
   
    const loginBtn = document.getElementById('loginButton');
    const loginModal = document.getElementById('loginModal');
    const closeModal = document.getElementById('closeModal');
    const loginForm = document.getElementById('loginForm');

   
    if (loginBtn && loginModal) {
        loginBtn.addEventListener('click', () => {
            loginModal.classList.add('active');
        });
    }

    
    if (closeModal && loginModal) {
        closeModal.addEventListener('click', () => {
            loginModal.classList.remove('active');
        });
    }

   
    if (loginModal) {
        loginModal.addEventListener('click', (e) => {
            if (e.target === loginModal) {
                loginModal.classList.remove('active');
            }
        });
    }

   
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault(); // Prevent actual submission / reload
            const username = document.getElementById('username').value;
            
            alert(`Welcome back, ${username}! (Practice Demo Login)`);
            loginForm.reset();
            loginModal.classList.remove('active');
        });
    }
});

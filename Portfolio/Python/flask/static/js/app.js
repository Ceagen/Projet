document.addEventListener('DOMContentLoaded', () => {
    const userIcon = document.getElementById('userIcon');
    const userIcon1 = document.getElementById('userIcon1');
    const loginOverlay = document.getElementById('loginOverlay');
    const loginOverlayMobile = document.getElementById('loginOverlayMobile');
    const closeLogin = document.getElementById('closeLogin');
    const closeLoginMobile = document.getElementById('closeLoginMobile');

    const forms = document.querySelectorAll('.needs-validation');

    Array.from(forms).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    userIcon.addEventListener('click', () => {
        loginOverlay.style.display = 'flex';
    });

    userIcon1.addEventListener('click', () => {
        loginOverlayMobile.style.display = 'flex';
    });

    closeLogin.addEventListener('click', () => {
        loginOverlay.style.display = 'none';
    });
    closeLoginMobile.addEventListener('click', () => {
        loginOverlayMobile.style.display = 'none';
    });

    // Optional: close if clicking outside form
    loginOverlay.addEventListener('click', (e) => {
        if (e.target === loginOverlay) {
            loginOverlay.style.display = 'none';
        }
    });
    loginOverlayMobile.addEventListener('click', (e) => {
        if (e.target === loginOverlayMobile) {
            loginOverlayMobile.style.display = 'none';
        }
    });

    //hamburger icon for mobile to display links on a mobile vw
    const menuToggle = document.querySelector('.menu-toggle');
    const navBar = document.querySelector('.navbar1');
    const mediaQuery = window.matchMedia('(max-width: 768px)');

    // Handle toggle click
    menuToggle.addEventListener('click', () => {
        const isActive = menuToggle.classList.toggle('active');

        if (getComputedStyle(navBar).display === 'flex') {
            navBar.style.display = 'none';
        } else {
            navBar.style.display = 'flex';
        }

        userIcon1.addEventListener('click', () => {
            loginOverlay.style.display = 'flex';
        });

        closeLogin.addEventListener('click', () => {
            loginOverlay.style.display = 'none';
        });
    });

    // Handle screen size change
    mediaQuery.addEventListener('change', (e) => {
        if (e.matches) {
            // On mobile — optionally hide the nav
            navBar.style.display = 'none';
        } else {
            // On desktop — always show nav and reset toggle
            navBar.style.display = 'none';
            menuToggle.classList.remove('active');
            if(e.matches && loginOverlay.style.display === 'none'){
                1+1
            }else{
                loginOverlayMobile.style.display = 'none';
                loginOverlay.style.display = 'none';
            }
        }
    });

    document.querySelector('.dropdown-button').addEventListener('click',()=>{
        toggleDropdown();
    })

    //drop down menu
    function toggleDropdown() {
        document.getElementById("dropdownMenu").classList.toggle("show");
    }

    // Close dropdown if clicked outside
    window.addEventListener("click", function(event) {
        if (!event.target.matches('.dropdown-button')) {
        const dropdowns = document.querySelectorAll(".dropdown-content");
        dropdowns.forEach(menu => menu.classList.remove("show"));
        }
    });
})
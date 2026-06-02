// Basic scripts for the poultry project
document.addEventListener('DOMContentLoaded', function() {
    console.log('Poultry project script loaded');
    
    // Auto-close mobile navbar on click
    const navLinks = document.querySelectorAll('.nav-link');
    const menuToggle = document.getElementById('navbarNav');
    const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle: false});
    
    navLinks.forEach((l) => {
        l.addEventListener('click', () => { 
            if (window.innerWidth < 992) {
                bsCollapse.toggle();
            }
        });
    });
});

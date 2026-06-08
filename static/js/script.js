// Basic scripts for the poultry project
document.addEventListener('DOMContentLoaded', function() {
    console.log('Poultry project initialized');
    
    // Smooth scroll for internal links if any
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            if (this.getAttribute('href') !== '#') {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});

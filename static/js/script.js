// Basic scripts for My Portfolio
document.addEventListener('DOMContentLoaded', function() {
    console.log('My Portfolio initialized');
    
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

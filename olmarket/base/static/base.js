document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.navbar a');

    links.forEach(link => {
        link.addEventListener('click', function() {
            links.forEach(l => l.classList.remove('active-nav-btn'));

            this.classList.add('active-nav-btn');

            localStorage.setItem('activeLink', this.href);
        });
    });

    const activeLink = localStorage.getItem('activeLink');
    if (activeLink) {
        links.forEach(link => {
            if (link.href === activeLink) {
                link.classList.add('active-nav-btn');
            }
        });
    }
});

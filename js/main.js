document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle Logic
    const themeToggles = document.querySelectorAll('#theme-toggle, #theme-toggle-mobile');
    const htmlElement = document.documentElement;
    
    // Check for saved theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    htmlElement.classList.toggle('dark', savedTheme === 'dark');
    
    themeToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const isDark = htmlElement.classList.toggle('dark');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            updateThemeIcons();
        });
    });

    function updateThemeIcons() {
        const sunIcons = document.querySelectorAll('.sun-icon');
        const moonIcons = document.querySelectorAll('.moon-icon');
        const isDark = htmlElement.classList.contains('dark');
        
        sunIcons.forEach(icon => {
            if (isDark) icon.classList.add('hidden');
            else icon.classList.remove('hidden');
        });
        
        moonIcons.forEach(icon => {
            if (isDark) icon.classList.remove('hidden');
            else icon.classList.add('hidden');
        });
    }
    updateThemeIcons();

    // RTL Toggle Logic
    const rtlToggles = document.querySelectorAll('#rtl-toggle, #rtl-toggle-mobile');
    rtlToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const isRtl = htmlElement.getAttribute('dir') === 'rtl';
            htmlElement.setAttribute('dir', isRtl ? 'ltr' : 'rtl');
            localStorage.setItem('dir', isRtl ? 'ltr' : 'rtl');
        });
    });
    
    // Check for saved direction
    const savedDir = localStorage.getItem('dir') || 'ltr';
    htmlElement.setAttribute('dir', savedDir);

    // Mobile Menu Logic
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
            mobileMenu.classList.toggle('flex');
        });
    }

    // Sidebar Toggle (Dashboard)
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebarClose = document.getElementById('sidebar-close');
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.getElementById('sidebar-overlay');

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', () => {
            sidebar.classList.toggle('active');
            if (overlay) overlay.classList.toggle('hidden');
        });
    }

    if (sidebarClose && sidebar) {
        sidebarClose.addEventListener('click', () => {
            sidebar.classList.remove('active');
            if (overlay) overlay.classList.add('hidden');
        });
    }

    if (overlay) {
        overlay.addEventListener('click', () => {
            sidebar.classList.remove('active');
            overlay.classList.add('hidden');
        });
    }

    // Smooth Scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Reveal on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                
                // Handle progress bar animations
                const progressBars = entry.target.querySelectorAll('.progress-bar-animate');
                progressBars.forEach(bar => {
                    const width = bar.getAttribute('data-width');
                    bar.style.width = width + '%';
                });

                // Handle counter animations
                const counters = entry.target.querySelectorAll('.counter');
                counters.forEach(counter => {
                    animateCounter(counter);
                });

                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale').forEach(el => observer.observe(el));

    // Counter Animation function
    function animateCounter(el) {
        const target = +el.getAttribute('data-target');
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;

        const update = () => {
            current += step;
            if (current < target) {
                el.innerText = Math.ceil(current).toLocaleString();
                requestAnimationFrame(update);
            } else {
                el.innerText = target.toLocaleString();
            }
        };
        update();
    }

    // Back to Top Logic
    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                backToTop.classList.add('show');
            } else {
                backToTop.classList.remove('show');
            }
        });

        backToTop.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
});

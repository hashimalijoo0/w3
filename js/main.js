document.addEventListener('DOMContentLoaded', () => {
    // Intro Overlay Logic
    const introOverlay = document.getElementById('intro-overlay');
    const hasVisited = localStorage.getItem('snowman_visited');

    if (introOverlay) {
        if (!hasVisited) {
            // First time visit
            setTimeout(() => {
                introOverlay.classList.add('hidden');
                localStorage.setItem('snowman_visited', 'true');
                // Remove from DOM after transition to avoid blocking clicks
                setTimeout(() => {
                    introOverlay.style.display = 'none';
                }, 1000);
            }, 3000); // Show for 3 seconds
        } else {
            // Already visited
            introOverlay.style.display = 'none';
        }
    }

    // Scroll Animation for Intro (if user scrolls before timeout)
    // Optional: If user scrolls, dismiss intro immediately
    window.addEventListener('scroll', () => {
        if (introOverlay && !introOverlay.classList.contains('hidden') && !hasVisited) {
            introOverlay.classList.add('hidden');
            localStorage.setItem('snowman_visited', 'true');
            setTimeout(() => {
                introOverlay.style.display = 'none';
            }, 1000);
        }
    });


    // --- Testimonial Slider Logic ---
    let slideIndex = 1;
    showSlides(slideIndex);

    // Next/previous controls
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    if (prevBtn && nextBtn) {
        prevBtn.addEventListener('click', () => plusSlides(-1));
        nextBtn.addEventListener('click', () => plusSlides(1));
    }

    // Dot controls
    const dots = document.querySelectorAll('.dot');
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => currentSlide(index + 1));
    });

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    function showSlides(n) {
        let i;
        let slides = document.getElementsByClassName("testimonial-slide");
        let dots = document.getElementsByClassName("dot");

        if (slides.length === 0) return; // Exit if no slides found

        if (n > slides.length) { slideIndex = 1 }
        if (n < 1) { slideIndex = slides.length }

        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
            slides[i].classList.remove("active");
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }

        slides[slideIndex - 1].style.display = "block";
        slides[slideIndex - 1].classList.add("active");
        if (dots.length > 0) {
            dots[slideIndex - 1].className += " active";
        }
    }

    // Auto Slide
    setInterval(() => {
        plusSlides(1);
    }, 5000); // Change image every 5 seconds

    // --- Burger Menu Logic ---
    const burger = document.querySelector('.burger-menu');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    if (burger) {
        burger.addEventListener('click', () => {
            // Toggle Nav
            nav.classList.toggle('nav-active');

            // Animate Links
            navLinks.forEach((link, index) => {
                if (link.style.animation) {
                    link.style.animation = '';
                } else {
                    link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
                }
            });

            // Burger Animation
            burger.classList.toggle('toggle');
        });

        // Close menu when a link is clicked
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                nav.classList.remove('nav-active');
                burger.classList.remove('toggle');
                navLinks.forEach((link) => {
                    link.style.animation = '';
                });
            });
        });
    }
});

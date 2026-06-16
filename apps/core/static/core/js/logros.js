// static/core/js/logros.js

document.addEventListener("DOMContentLoaded", function () {
    const counters = document.querySelectorAll(".number");

    const animate = (el) => {
        const target = +el.getAttribute("data-target");
        const dur = 1800;
        const start = performance.now();

        const tick = (now) => {
            const p = Math.min((now - start) / dur, 1);
            const ease = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.round(ease * target);
            if (p < 1) requestAnimationFrame(tick);
        };

        requestAnimationFrame(tick);
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                animate(e.target);
                observer.unobserve(e.target);
            }
        });
    }, { threshold: 0.3 });

    counters.forEach(el => observer.observe(el));
});
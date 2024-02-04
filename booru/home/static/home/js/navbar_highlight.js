// Highlight the active link in the navbar
document.addEventListener("DOMContentLoaded", function () {
    const currentPath = window.location.pathname;
    const navbarLinks = document.querySelectorAll(".navbar-nav .nav-link");

    navbarLinks.forEach((link) => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
            link.style.color = "white"; // Change to the desired color
        }
    });
});
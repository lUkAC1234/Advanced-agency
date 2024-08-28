document.addEventListener("DOMContentLoaded", () => {
    const selectButton = document.querySelector(".select-button");
    const dropdownContent = document.querySelector(".language-dropdown-content");
    const closeButton = document.querySelector(".language-dropdown-content-close");

    selectButton.addEventListener("click", () => {
        dropdownContent.classList.toggle("show");
    });

    closeButton.addEventListener("click", () => {
        dropdownContent.classList.remove("show");
    });

    dropdownContent.addEventListener("click", event => {
        const target = event.target;
        if (target.classList.contains("language-option")) {
            const value = target.getAttribute("value");
            selectButton.textContent = target.textContent;
            document.querySelector("#language_select").value = value;
            document.getElementById("language_form").submit();
        }
    });
});

const className = "header-active";
const BtnTop = "btn-top-active";
const scrollTrigger = 60;
const scrollBtn = 100;
const backToTopButton = document.getElementById('back-to-top');
const siteProgressBar = document.getElementById('progress');
const contactForm = "active";

window.addEventListener('scroll', () => {
    const scrolled = window.scrollY >= scrollTrigger || window.pageYOffset >= scrollTrigger;
    const showBtnTop = window.scrollY >= scrollBtn || window.pageYOffset >= scrollBtn;

    document.getElementById("header").classList.toggle(className, scrolled);
    siteProgressBar.classList.toggle("progress-hidden", !scrolled);
    siteProgressBar.style.background = scrolled ? 'var(--progress-background)' : '';

    document.getElementById("btn-top-container").classList.toggle(BtnTop, showBtnTop);
    document.getElementById("included-section").classList.toggle(contactForm, showBtnTop);
});

backToTopButton.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

const siteHeader = document.getElementById('header');
const dropdownMenu = document.getElementById('dropdown__menu');
let lastScrollPosition = 0;
const screenWidthThreshold = 1400;

window.addEventListener('scroll', () => {
    if (window.innerWidth <= screenWidthThreshold) {
        siteHeader.style.transform = 'translateY(0)';
    } else {
        const currentScrollPosition = window.scrollY;

        if (currentScrollPosition > lastScrollPosition) {
            siteHeader.style.transform = 'translateY(-100%)';
            siteProgressBar.style.bottom = '0';
            siteProgressBar.style.top = 'unset';
            siteProgressBar.style.transform = 'translateY(5px)';
            if (dropdownMenu) dropdownMenu.style.transform = 'translateY(-120%)';
        } else {
            siteHeader.style.transform = 'translateY(0)';
            siteProgressBar.style.top = '0';
            siteProgressBar.style.bottom = 'unset';
            siteProgressBar.style.transform = 'translateY(0px)';
            if (dropdownMenu) dropdownMenu.style.transform = 'translateY(0)';
        }
        lastScrollPosition = currentScrollPosition;
    }
});

const navLinks = document.querySelectorAll('.nav-link');

navLinks.forEach(link => {
    if (link.href === window.location.href) {
        link.classList.add('active');
    }
});

const hamburger = document.getElementById('hamburger');
const icon = document.getElementById('hamburgerIcon');
const pagesSection = document.querySelector('.pages-section-container');

hamburger.addEventListener('click', () => {
    pagesSection.classList.toggle('active');
    icon.classList.toggle('fa-bars-staggered');
    icon.classList.toggle('fa-xmark');
});

const dropdownProfileImage = document.getElementById('dropdownProfileImage');

const showDropdown = (contentId, buttonId) => {
    const dropdownContent = document.getElementById(contentId);
    const dropdownButton = document.getElementById(buttonId);

    dropdownButton.addEventListener('click', () => {
        dropdownContent.classList.toggle('show-dropdown');
        dropdownProfileImage.classList.toggle('active');
    });
};

showDropdown('dropdown-content', 'dropdown-button');

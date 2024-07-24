document.addEventListener('DOMContentLoaded', function () {
    const modalOverlay = document.getElementById('pricingDetailModalOverlay');
    const videoContainer = document.querySelector('.pricing-detail-first-screen-video-container');
    const video = videoContainer.querySelector('video');
    const videoOverlay = videoContainer.querySelector('.video-color-overlay');
    let isModalOpen = false; 

    function setOverlayColor(color) {
        videoOverlay.style.backgroundColor = color;
    }

    function checkVideoLoaded() {
        if (video.readyState >= 3) {
            setOverlayColor('var(--background-purple)');
        } else {
            setOverlayColor('var(--background-white)');
        }
    }

    video.addEventListener('canplay', checkVideoLoaded);
    video.addEventListener('loadeddata', checkVideoLoaded);
    video.addEventListener('error', function() {
        setOverlayColor('var(--background-white)');
    });

    checkVideoLoaded();

    function toggleModal() {
        isModalOpen = !isModalOpen;
        if (isModalOpen) {
            modalOverlay.classList.add('active');
        } else {
            modalOverlay.classList.remove('active');
        }
    }

    document.querySelectorAll('.open-form-button').forEach(button => {
        button.addEventListener('click', toggleModal);
    });

    document.querySelector('.pricing-detail-close-form-button').addEventListener('click', function () {
        isModalOpen = false;
        modalOverlay.classList.remove('active');
    });

    window.addEventListener('click', function (event) {
        if (event.target === modalOverlay) {
            isModalOpen = false;
            modalOverlay.classList.remove('active');
        }
    });
});

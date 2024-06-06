document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contact-form-included');
    const toggleButton = document.getElementById('contact-form-included-toggle');
    const closeButton = document.getElementById('contact-form-included-close');

    const toggleForm = () => form.classList.toggle('active');
    const closeForm = event => !form.contains(event.target) && !toggleButton.contains(event.target) && form.classList.remove('active');

    toggleButton.addEventListener('click', toggleForm);
    closeButton.addEventListener('click', toggleForm);
    document.addEventListener('click', closeForm);
});

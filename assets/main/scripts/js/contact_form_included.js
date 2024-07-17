document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contact-form-included');
    const toggleButtons = [
        document.getElementById('contact-form-included-toggle'),
        document.getElementById('contact-form-included-toggle-index')
    ];
    const closeButton = document.getElementById('contact-form-included-close');

    const toggleForm = () => form?.classList.toggle('active');

    const closeForm = event => {
        if (form && !form.contains(event.target) && !toggleButtons.some(button => button?.contains(event.target))) {
            form.classList.remove('active');
        }
    };

    toggleButtons.forEach(button => button?.addEventListener('click', toggleForm));
    closeButton?.addEventListener('click', toggleForm);
    document.addEventListener('click', closeForm);
});

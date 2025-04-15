
const alertButtons = document.querySelectorAll('.alert button');
alertButtons.forEach(button => {
    button.addEventListener('click', () => {
        const alertTarget = button.dataset.dismissTarget;
        const alert = document.querySelector(alertTarget);
        alert.remove();
    });
});

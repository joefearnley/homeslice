
const accountMenuButton = document.getElementById('user-menu-button');

accountMenuButton.addEventListener('click', e => {
    console.log('Account menu button clicked');

    const accountMenu = document.getElementById('user-dropdown');
    if (accountMenu.classList.contains('hidden')) {
        accountMenu.classList.remove('hidden');
    } else {
        accountMenu.classList.add('hidden');
    }
});
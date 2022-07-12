"use strict"

showActiveLink('menu')

// показать активную ссылку
function showActiveLink(menu) {
    try {
        let elem = document.getElementById(menu).querySelectorAll('a');
        let url = document.location.href;
        for (const link of elem) {
            if (url === link.href) {
                link.classList.add('active');
            };
        };
    } catch (e) { }
}
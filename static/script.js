console.log('hello')
$(document).ready(function () {
    $('#div1').hide().fadeIn(2000);
    $('.carousel').carousel({
        interval: false
    });



});
var contact =
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

function debounce_leading(func, timeout = 0) {
    let timer;
    return (...args) => {
        if (!timer) {
            func.apply(this, args);
        }
        clearTimeout(timer);
        timer = setTimeout(() => {
            timer = undefined;
        }, timeout);
    };
}
const slideInDivs = document.querySelectorAll('.content-container');
function checkScroll(e) {
    slideInDivs.forEach(slideInDiv => {
        const slideInAt = (window.scrollY + window.innerHeight) - slideInDiv.scrollHeight / 2;
        const divBottom = slideInDiv.offsetTop + slideInDiv.scrollHeight;
        const isHalf = slideInAt > slideInDiv.offsetTop;
        const isNotScrolledPast = window.scrollY < divBottom;
        if (isHalf && isNotScrolledPast) {
            slideInDiv.classList.add('active');
        };
    });
};

window.addEventListener('scroll', debounce_leading(checkScroll));

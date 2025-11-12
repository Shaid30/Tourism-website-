const menuIcon = document.getElementById('menuIcon');
const navLinks = document.getElementById('navLinks');

menuIcon.onclick = () => {
    navLinks.classList.toggle('active');
}


const hero = document.querySelector(".hero");

let i = 0;

hero.style.backgroundImage = `url('${images[i]}')`;

setInterval(() => {
    i = (i + 1) % images.length;
    hero.style.backgroundImage = `url('${images[i]}')`;
}, 5000);



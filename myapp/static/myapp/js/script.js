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

document.querySelectorAll(".btn-more").forEach(btn => {
    btn.addEventListener("click", function () {
        const card = this.closest(".card");
        const desc = card.querySelector(".desc");

        desc.classList.toggle("expanded");

        this.textContent = desc.classList.contains("expanded")
            ? "Show Less"
            : "Read More";
    });
});


document.querySelectorAll(".btn-book").forEach(btn => {
    btn.addEventListener("click", function () {
        const title = this.closest(".card").querySelector(".title").textContent;
        alert("Booking started for: " + title);
    });
});



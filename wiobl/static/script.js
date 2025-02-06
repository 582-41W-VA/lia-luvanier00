// Toggle burger menu for smaller screen sizes
function toggleBurger() {
    const burger = document.getElementById("burger");
    const menuList = document.getElementById("menu-list");

    if (window.innerWidth > 1100) {
        menuList.classList.remove("menu-hidden");
        burger.style.display = "none";
    } else {
        menuList.classList.add("menu-hidden");
        burger.style.display = "block";
    }
}

// Handle burger menu toggle click.
function handleBurgerClick() {
    const burger = document.getElementById("burger");
    const menuList = document.getElementById("menu-list");

    burger.addEventListener("click", () => {
        menuList.classList.toggle("menu-hidden");
        menuList.classList.toggle("menu-list-js");
    });
}

// Run functions to handle burger menu when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    toggleBurger();
    handleBurgerClick();
});

// Run `toggleBurger` whenever the window is resized
window.addEventListener("resize", toggleBurger);


// map api
document.addEventListener('DOMContentLoaded', function () {
    const coordinates = [45.46120974762705, -73.80929962254508];
    const locationName = 'Lakeside Heights, Pointe-Claire, QC';

    const map = L.map('map', {
        layers: [
            L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                'attribution': 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors'
            })
        ],
        center: coordinates,
        zoom: 15
    });

    const marker = L.marker(coordinates)
    .addTo(map)
    .bindPopup(locationName)
    .openPopup();
});

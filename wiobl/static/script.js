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

// Run ⁠ toggleBurger ⁠ whenever the window is resized
window.addEventListener("resize", toggleBurger);


// map api
document.addEventListener('DOMContentLoaded', function () {
    const coordinates_court_1 = [45.46120974762705, -73.80929962254508];//Pointe Claire Park
    const coordinates_court_2 = [45.48934050768304, -73.85824621609802];//Pierrefonds-Roxboro Park
    const coordinates_court_3 = [45.48272170531596, -73.8067795278847];//Dollard-Ddes-Ormeaux Park
    const coordinates_court_4 = [45.44387748895584, -73.8607540133765];//Kirkland Park
    const locationName_1 = 'Lakeside Heights, Pointe-Claire, QC';
    const locationName_2 = 'Parc Ménard, Pierrefonds-Roxboro, QC';
    const locationName_3 = 'Dollard-Ddes-Ormeaux, QC';
    const locationName_4 = 'Kirkland, QC';

    const map = L.map('map', {
        layers: [
            L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                'attribution': 'Map data ©️ <a href="https://openstreetmap.org">OpenStreetMap</a> contributors'
            })
        ],
        center: coordinates_court_1,
        zoom: 12
    });

    const marker_1 = L.marker(coordinates_court_1)
        .addTo(map)
        .bindPopup(locationName_1)
        .openPopup();

    const marker_2 = L.marker(coordinates_court_2)
        .addTo(map)
        .bindPopup(locationName_2)
        .openPopup();

    const marker_3 = L.marker(coordinates_court_3)
        .addTo(map)
        .bindPopup(locationName_3)
        .openPopup();

    const marker_4 = L.marker(coordinates_court_4)
        .addTo(map)
        .bindPopup(locationName_4)
        .openPopup();
});
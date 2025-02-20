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

// Run ⁠ toggleBurger ⁠ whenever the window is resized
window.addEventListener("resize", toggleBurger);

// Run functions to handle burger menu when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    toggleBurger();
    handleBurgerClick();
});

// map api
document.addEventListener('DOMContentLoaded', function () {

    const map = L.map('map', {
        layers: [
            L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                'attribution': 'Map data ©️ <a href="https://openstreetmap.org">OpenStreetMap</a> contributors'
            })
        ],
        center: [45.46120974762705, -73.80929962254508],
        zoom: 12
    });

    fetch("http://127.0.0.1:8000/wioblapp/api/parks")
        .then(response => response.json())
        .then(data => {
            data.forEach(park => {
                const lat = parseFloat(park.latitude);
                const lon = parseFloat(park.longitude);

                L.marker([lat, lon])
                    .addTo(map)
                    .bindPopup(`<b>${park.name}</b><br>${park.address}`)
                    .openPopup();
            });

            if (data.length > 0) {
                map.setView([parseFloat(data[0].latitude), parseFloat(data[0].longitude)], 12);
            }
        })

        .catch(error => console.error("Error connect API data locations:", error));
});

// * * * * * * * * COMMENTS * * * * * * * * 

// Display "edit comment" input
function displayEditComment() {
    const editContainers = document.querySelectorAll("#comment-edit");
    const editBtns = document.querySelectorAll("#edit-btn");

    editBtns.forEach((editBtn, index) => {
        editBtn.addEventListener("click", () => {
            editContainers[index].style.display = "block";
        });
    });
}

displayEditComment();

// Open popup for flagging comments when flag is clicked.
function openPopupFlag() {
    const popups = document.querySelectorAll("#popup");
    const flagIcons = document.querySelectorAll("#flag-icon");

    flagIcons.forEach((flagIcon, index) => {
        flagIcon.addEventListener("click", () => {
            popups[index].style.display = "block";
        });
    });
}

openPopupFlag();

// Cancel popup for flagging comments when cancel button is clicked.
function cancelPopupFlag() {
    const popups = document.querySelectorAll("#popup");
    const cancelPopupBtns = document.querySelectorAll("#cancel-popup");

    cancelPopupBtns.forEach((cancelPopupBtn, index) => {
        cancelPopupBtn.addEventListener("click", () => {
            popups[index].style.display = "none";
        });
    });
}

cancelPopupFlag();

// Apply the CSS styles to make the message into a popup element if javascript is available.
function stylePopupFlag() {
    const popups = document.querySelectorAll("#popup");

    popups.forEach((popup) => {
        popup.style.display = "none";
        popup.style.position = "absolute";
        popup.style.right = "10%";
        popup.style.zIndex = "10";
        popup.style.padding = "24px";

        if (window.innerWidth < 992) {
            popup.style.left = "10%";
        }

    });

    const flagIcons = document.querySelectorAll("#flag-icon");
    flagIcons.forEach((flagIcon) => {
        flagIcon.style.display = "block";
    });
}

stylePopupFlag();
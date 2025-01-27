function toggleBurger () {
    var burger = document.getElementById("burger");
    var menuList = document.getElementById("menu-list");

    menuList.classList.replace("menu-list-nojs", "menu-list-js");
    burger.classList.replace("burger-nojs", "burger-js");

    burger.addEventListener("click", (event) => {
        menuList.classList.toggle("menu-active");
    });
    
}

toggleBurger();
document.getElementById("year").textContent = new Date().getFullYear();
const toggle = document.querySelector(".nav-toggle");
const nav = document.querySelector("header nav");
if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const isOpen = nav.style.display === "block";
    nav.style.display = isOpen ? "none" : "block";
  });
}

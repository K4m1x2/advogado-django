window.addEventListener("scroll", function(){
    var header = document.querySelector(".main-image")
    header.classList.toggle("sticky", window.scrollY > 0)
})
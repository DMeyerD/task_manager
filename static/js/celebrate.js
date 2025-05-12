document.querySelectorAll(".complete-button").forEach(button => {
    button.addEventListener("click", function(){
        button.classList.add("rotate-on-click");

        setTimeout(() => {
            button.classList.remove("rotate-on-click");
        },400); // must match animation duration

        confetti({
            particleCount: 75,
            speed: 60,
            origin: {y: 0.6}
        });
    });
});
const blueLed = document.getElementById("blueLed");
const redLed = document.getElementById("redLed");
const greenLed = document.getElementById("greenLed");
const yellowLed = document.getElementById("yellowLed");

const leds = [blueLed, redLed, greenLed, yellowLed];

leds.forEach(led => {
    led.addEventListener("click", () => toggleLed(led));
})

function toggleLed(led) {
    led.classList.toggle("off");
}
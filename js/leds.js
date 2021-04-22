const blueLed = document.getElementById("blueLed");
const redLed = document.getElementById("redLed");
const greenLed = document.getElementById("greenLed");
const yellowLed = document.getElementById("yellowLed");

const leds = [blueLed, redLed, greenLed, yellowLed];

const client = new HttpClient();

const ws = websocket();

leds.forEach(led => {
    led.addEventListener("click", () => toggleLed(led));
    client.get(`/state?led=${led.dataset.color}`, (newState) => {
        led.dataset.state = newState;
    })
})

function toggleLed(led) {
    client.get(`/toggle?led=${led.dataset.color}`, (newState) => {
        led.dataset.state = newState;
        ws.send(`{"${led.dataset.color}": "${newState}"}`);
    });
}

function websocket() {
    const ws = new WebSocket("ws://raspberrypi:8082/live");
    ws.onmessage = function (event) {
        const ledStates = JSON.parse(event.data);
        leds.forEach(led => {
            const colorList = Object.keys(ledStates).map(c => c.toLowerCase());
            const key = led.dataset.color.toLowerCase();
            if (colorList.includes(key)) {
                led.dataset.state = ledStates[key];
            }
        });
    };
    return ws;
}

function HttpClient() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() { 
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }

        anHttpRequest.open( "GET", aUrl, true );            
        anHttpRequest.send( null );
    }
}
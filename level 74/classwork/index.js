// საკლასო დავალება:

// html-ის სტრუქტურაში დაამატეთ ერთი პარაგრაფი და მას გაუწერეთ id.

// js-ში წამოიღეთ ეს პარაგრაფი და მას გაუწერეთ onmouseover event handler. ამ event handler-ს გადაეცით ფუნქცია, რომელიც ვებსაიტზე ტექსტს განალაგებს ცენტრში
let paragraph = document.getElementById("p-1");

paragraph.onmouseover = centerText;

function centerText() {
    paragraph.style.textAlign = "center";
}

let button = document.getElementById("dark");

button.addEventListener("click", function(event) {
    console.log(event);
    document.body.style.backgroundColor = "black";
    document.body.style.color = "white";
});

// საკლასო დავალება:

// html-ის სტრუქტურაში დაამატეთ ლინკი, რომელსაც გაუწერეთ id-ს, სტილს, href-ს. 

// ეს ელემენტი წამოიღეთ js-ში და მასზე დაამატეთ მოვლენის მსმენელი. მოვლენა უნდა იყოს pointerover, ხოლო ფუნქციას გაუწერეთ e პარამეტრი.

// ამ პარამეტრით მიწვდით target და დაბეჭდეთ ელემენტის ყველა ატრიბუტის მნიშვნელობა, ბოლოს დაბეჭდეთ თვითონ target.

let link = document.getElementById("myLink");

link.addEventListener("pointerover", function(e) {
    const target = e.target;


    for (let attr of target.attributes) {
        console.log(attr.name + ": " + attr.value);
    }

    console.log("Target element:", target);
});
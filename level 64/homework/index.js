let hobby = prompt("enter youur hobby")
alert(hobby)

let name = prompt("enter your name: ")
let surname = prompt("enter your surname: ")

alert(name + " " + surname)

let message = prompt("Enter your message: ");
document.querySelector("p").textContent = message;

let emoji = prompt("enter your fav emoji: ")
alert (emoji + "thank u")


let title = prompt("enter website title: ")
document.title = a

document.getElementById('niga').addEventListener('click', () => {
    const txt = document.getElementById('textInput').value;
    alert(txt);
});

document.getElementById('form7').addEventListener('submit', (e) => {
    e.preventDefault();
    const color = document.getElementById('bgColor').value;
    document.body.style.backgroundColor = color;
});


document.getElementById('btn8').addEventListener('click', () => {
    const first = document.getElementById('firstName').value.trim();
    const last  = document.getElementById('lastName').value.trim();
    if (!first || !last) {
    alert('Please fill out both names!');
    return;
    }
    document.getElementById('fullName').textContent = `${first} ${last}`;
});
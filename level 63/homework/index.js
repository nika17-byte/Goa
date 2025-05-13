// 2) Create a function that displays an alert saying "Hello, world!".
function greet () {
    alert("hello world")
}

greet()
// 3) Write a function that takes a name as a parameter and logs "Hello, [name]!" to the console.
function welcome (name) {
    alert("hello " + name)
}

welcome ("nika")
// 4) Create a function that adds two numbers and returns the result.
function sum (num1, num2) {
    console.log (num1 + num2)
}

sum (7, 10)
// 5) Write a function that multiplies a number by 10 and returns the value.
function multiplication (num1) {
    console.log (num1  * 10)
}

multiplication (7)
// 6) Create an external JavaScript file and link it to an HTML file.
// 7) Move a function from the HTML file’s <script> tag into an external .js file.
// 8) Create multiple functions in an external JS file and call them from different buttons in your HTML page.
// 9) In your external JS file, write a function that changes the text of a paragraph when a button is clicked.
function divide(num1, num2) {
    console.log(num1 / num2)
}

function change () {
    let a = document.getElementById("p1")
    a.textContent = "kfc"
}
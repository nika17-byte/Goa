// საკლასო დავალება:
// შექმენით greet ფუნქცია, რომელიც პარაგრაფს შეუცვლის კონტენტს და ის გახდება "welcome {თქვენი სახელი}!".
// ეს ფუნქცია ჩაწერეთ external js-ის მეთოდით.
// როდესაც პარაგრაფს დავაკლიკებთ, უნდა გამოიძახოს ეს ფუნქცია
function greet() {
    let paragraph = document.getElementById("greeting");
    paragraph.textContent = "Welcome,nika"
}
document.addEventListener("DOMContentLoaded", function () {
    let paragraph = document.getElementById("greeting");
    paragraph.addEventListener("click", greet);
});
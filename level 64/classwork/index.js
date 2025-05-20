function handleSubmit(event) {
    event.preventDefault();

    let input = document.getElementById('username');
    console.log("input", input.value);
}
// საკლასო დავალება:
// შექმენით ფუნქცია სახელად concStrings. ფუნქციაში უნდა გქონდეთ ორი ცვლადი და 
// ორივეში შეინახეთ prompt-ით შემოტანილი ინფორმაცია. საბოლოოდ დაბეჭდეთ ამ ორი ცვლადის კონკატინაციის შედეგი alert box-ში
function concStrings() {
    let str1 = prompt("Enter 1st string:");
    let str2 = prompt("Enter 2nd string:");
    let result = str1 + str2;
    alert("result: " + result);
}
concStrings()
// 2-6)
// Create a counter that logs numbers from 1 to 5 to the console every second, then stops.
let count = 1;
const counter = setInterval(function() {
    console.log(count);
    if (count === 5) {
        clearInterval(counter);
    }
    count++;
}, 1000);
// Make a message display in the console every 2 seconds, and stop it after 10 seconds.
let messageInterval = setInterval(function() {
    console.log("This message appears every 2 seconds");
}, 2000);

setTimeout(function() {
    clearInterval(messageInterval);
}, 10000);
// Change the background color of a web page every 3 seconds, and stop changing after 5 changes.
let colorChanges = 0;
let colors = ["lightblue", "lightgreen", "lightcoral", "lightgoldenrodyellow", "lightgray"];
let bgInterval = setInterval(function() {
    document.body.style.backgroundColor = colors[colorChanges % colors.length];
    colorChanges++;
    if (colorChanges === 5) {
        clearInterval(bgInterval);
    }
}, 3000);
// Display the current time in the console every second, and stop after 15 seconds.

// Create a simple timer that counts up in seconds and stops when it reaches 10 seconds.
let seconds = 0;
let timer = setInterval(function() {
    seconds++;
    console.log("Timer: " + seconds + " second(s)");
    if (seconds === 10) {
        clearInterval(timer);
    }
}, 1000);
// 7-10)

// Create an array of 4 numbers and log the value of the second element.
const array1 = [1,2,3,4];
console.log(array1[1]);
// Change the value of the first element in an array to 100 and log the entire array.
array1[0] = 100;
console.log(array1)
// Create an array of 3 strings and log each one using individual console.log() statements with direct indexing.
const strings = ["nika" , "samkharadze" , "basketball"]
console.log(strings[0])
console.log(strings[1])
console.log(strings[2])
// Create an array of 5 numbers and find the sum of the first and last elements using indexing.
const array2 = [5,6,7,8,9]
console.log(array2[0] + array2[4])
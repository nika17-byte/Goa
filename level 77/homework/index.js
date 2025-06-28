// // 1. Countdown Timer:
// Create a countdown from 10 to 0 using setInterval. Log each number every second. When it reaches 0, stop the interval and log "Time's up!".
let count = 10;
const timer = setInterval(function() {
    console.log(count);
    if (count === 0) {
        clearInterval(timer);
        console.log("Time's up!");
    }
    count--;
}, 1000);
// 2. Flashing Title:
// Change the document.title between "Hello" and "Goodbye" every 1 second. After 6 seconds, stop the interval.
let toggle = true;
const flash = setInterval(function() {
    document.title = toggle ? "Hello" : "Goodbye";
    toggle = !toggle;
}, 1000);

setTimeout(function() {
    clearInterval(flash);
}, 6000);
// 3. Move a Box (Optional DOM Task):
// Create a box (div) and move it 10px to the right every 200ms using setInterval. Stop after it moves 100px.
let distance = 0;
const box = document.getElementById("box");
const move = setInterval(function() {
    distance += 10;
    box.style.left = distance + "px";
    if (distance >= 100) {
        clearInterval(move);
    }
}, 200);
// 4. Random Number Logger:
// Log a random number between 1 and 10 every 1.5 seconds. Stop it after 5 numbers are logged.
let countRand = 0;
const randomLog = setInterval(function() {
  const num = Math.floor(Math.random() * 10) + 1;
    console.log(num);
    countRand++;
    if (countRand >= 5) {
        clearInterval(randomLog);
    }
}, 1500);
// 5. Array to Uppercase:
// Create an array of 3 lowercase strings. Use a loop to convert each to uppercase and log them.
const arr = ["apple", "banana", "cherry"];
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i].toUpperCase());
}
// 6. Replace Middle Element:
// Create an array of 3 numbers. Replace the middle number with 0. Log the array.
const numbers = [5, 9, 3];
numbers[1] = 0;
console.log(numbers);
// 7. Add and Remove Elements:
// Create an array with 2 elements. Add one element to the end and one to the beginning. Then remove the last one. Log the final array.
const arr2 = ["a", "b"];
arr2.push("c");
arr2.unshift("z");
arr2.pop();
console.log(arr2); 
// 8. Average of Array:
// Create an array of 4 numbers. Calculate and log the average.
const nums = [10, 20, 30, 40];
let sum = 0;
for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
}
const average = sum / nums.length;
console.log(average);
// 9. Reverse an Array Manually:
// Create an array of 3 elements and manually (not using .reverse()) log the elements in reverse order using indexing.
const letters = ["x", "y", "z"];
console.log(letters[2]);
console.log(letters[1]);
console.log(letters[0]);
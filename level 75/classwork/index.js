    function printName() {
        console.log("Nikoloz samkharadze");
    }

    let intervalId = setInterval(printName, 10000);

    document.getElementById("stopButton").addEventListener("click", function() {
        clearInterval(intervalId); 
        console.log("Interval stopped");
    });

const array = [
    "Hello",                
    14,                     
    true,                   
    { name: "Nikolozi" },   
    [1, 2, 3]              
];


console.log(array);
function traverseArr(array) {
    for (let i = 0; i < array.length; i++) {
        console.log(array[i]); // Print each element
    }
}

traverseArr(["apple", "banana", "kiwi"]);
traverseArr([10, 20, 30, 40])
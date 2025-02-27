//const Display = document.getElementById("display"); isn't really necessary since js already selects the value

function appendToDisplay(input){
    display.value += input; // here we assign the basic input a value that should be displayed
}
function clearDisplay(){
    display.value="";
}
function calculate(){
    display.value = eval(display.value);
}
function deleteDisplay(){
    display.value = display.value.toString().slice(0, -1);//delete one caracter starting from 0 to the last caracter "-1"
}
function sqrt(){
    display.value = Math.sqrt(display.value);//this function calculates the square root of numbers
}
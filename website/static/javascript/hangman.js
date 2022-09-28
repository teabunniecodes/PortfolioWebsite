// const words = loadStrings(textdocuments/hangman-wordlist.txt)
const keyboardButton = document.getElementsByClassName("keyboard-button")
const guessLetter = document.getElementById("letter-guess")
const letterList = document.getElementById("letter-list")
const turnsLeft = document.getElementById("turns-left")
const guessList = []
let turns = 6
document.onkeyup = checkKey
// document.onkeyup = submitGuess
document.onkeydown = colorButton
document.addEventListener = checkButton()


// What I want to accomplish in hangman GUI
// buttons to flash if cooresponding key is pressed (can I use key value to = button value?)
    // figure out if I can have CSS on JS side (use inner HTML tag to add the style?)
    // when button is pressed, activates a guess as well
    // changes colors for the buttons if it is a correct guess or wrong guess (green/red)
// need to check the guess with the list of letter guesses already for duplicate letters
// need to check the letters with the word on server side to see if it is in the word
// create a way to have the user guess an entire word - have Enter and Backspace active during this time
// checks guessed word against server side word - if wrong Game over automatically

function checkButton() {
    for (let x=0; x < keyboardButton.length; x++) {
        keyboardButton[x].addEventListener("click", e => {
            validGuess(keyboardButton[x].value);
            addGuess(keyboardButton[x].value);
            let button = document.getElementById(keyboardButton[x].id)
            let classes = button.classList
            if (button.classList != "colored-button") {
                classes.toggle("colored-button", "keyboard-button")
            }
        });
    }
}

function colorButton(e) {
    let button = document.getElementById(e.key)
    let classes = button.classList
    if ((e.key == button.value) && (button.classList != "colored-button")) {
        classes.toggle("colored-button", "keyboard-button");
    }
}

function checkKey(e) {
    if ((e.keyCode >= 65 && e.keyCode <= 90) || (e.keyCode >= 97 && e.keyCode <= 122)) {
        colorButton(e)
        console.log(e.key + " is a letter");
        validGuess(e.key);
        addGuess(e.key);
    }
}

// function submitGuess(e)
//     if (e.keyCode == 13) {
//             console.log(e.key + " is Enter");
//             return e.keyCode;
//         }
//     else if (e.keyCode == 8) {
//             console.log(e.key + " is Backspace");
//             return e.keyCode;
//         }

function validGuess(guess) {
    // guessList.push(guess);
    guessLetter.innerHTML = `you guessed - ${guess.toUpperCase()}`;
}

function addGuess(guess) {
    if (guessList.includes(guess)) {
        console.log("You already guessed this");
    }
    else {
        turnsLeft.innerHTML = `Turns Left : ${turns}`
        guessList.push(guess.toUpperCase());
        letterList.innerHTML = `${guessList}`;
    }
}

function gameOver() {
    if (turns == 0) {
        turnsLeft.innerHTML = `Turns Left : ${turns}`;
        guessLetter.innerHTML = `GAME OVER D:`;
    }
}
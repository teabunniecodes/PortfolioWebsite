// const words = loadStrings(textdocuments/hangman-wordlist.txt)
const keyboardButton = document.getElementsByClassName("keyboard-button")
const guessLetter = document.getElementById("letter-guess")
const letterList = document.getElementById("letter-list")
const turnsLeft = document.getElementById("turns-left")
const guessList = []
let turns = 6
let button = "x"
let classes = "y"
let guessWord = false
document.onkeyup = checkKey
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
            button = document.getElementById(keyboardButton[x].id)
            classes = button.classList
            if (button.classList != "colored-button") {
                classes.toggle("colored-button", "keyboard-button")
            }
        });
    }
}

function checkKey(e) {
    if (turns > 0) {
        if ((e.keyCode >= 65 && e.keyCode <= 90) || (e.keyCode >= 97 && e.keyCode <= 122) && (guessWord == false)) {
            validGuess(e.key);
            button = document.getElementById(e.key);
            classes = button.classList;
            if ((e.key == button.id) && (button.classList != "colored-button")) {
                classes.toggle("colored-button", "keyboard-button");
            }
        }
        else if (e.key === "Shift") {
            console.log("Shift was pressed")
            if (guessWord == false) {
                guessWord = true
            }
            else {
                guessWord = false
            }
        }
        if (guessWord == true) {
            if (e.key === "Enter") {
                console.log(e.key + " is Enter");
                console.log("This needs to check for the length of the word in future as well")
                guessWord = false
                // return e.keyCode;
            }
            else if (e.key === "Backspace") {
                console.log(e.key + " is Backspace");
                return e.keyCode;
            }
        }
    }
}

// function submitGuess(e) {
    
// }

function validGuess(guess) {
    guess = guess.toUpperCase()
    if (turns > 0){
        if (guessList.includes(guess)) {
            guessLetter.innerHTML = `You already guessed the letter ${guess}.  You want to waste a turn???`;
        }
        else {
            guessList.push(guess);
            turns -= 1;
            turnsLeft.innerHTML = `Turns Left : ${turns}`;
            guessLetter.innerHTML = `you guessed - ${guess}`;
            letterList.innerHTML = `${guessList}`;
            if (turns == 0) {
                gameOver()
            }
        }
    }
}

function gameOver() {
    if (turns == 0) {
        turnsLeft.innerHTML = `Turns Left : ${turns}`;
        guessLetter.innerHTML = `GAME OVER D:`;
    }
}
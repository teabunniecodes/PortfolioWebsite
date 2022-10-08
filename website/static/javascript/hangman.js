const keyboardButton = document.getElementsByClassName("keyboard-button")
const keyboardAction = document.getElementsByClassName("keyboard-action")
const guessLetter = document.getElementById("letter-guess")
const letterList = document.getElementById("letter-list")
const turnsLeft = document.getElementById("turns-left")
const gameBoard = document.getElementById("game-board")
const gameStart = document.getElementById("game-start")
const gamePlay = document.getElementById("game-play")
const guessList = []
let turns = 6
let button = "x"
let classes = "y"
let className = "colored-button"
let guessWord = false
document.onkeyup = checkKey

function startGame() {
    gamePlay.addEventListener ("click", e=> {
        gameStart.style.display = "none";
        switchViews();
    });
}

function checkButton() {
    // Need to fix so the buttons no longer change colors if turns are 0
    for (let x=0; x < keyboardButton.length; x++) {
        keyboardButton[x].addEventListener("click", e => {
            alphabetEvent(keyboardButton[x].id)
            });
        }
    for (let x=0; x < keyboardAction.length; x++) {
        keyboardAction[x].addEventListener("click", e => {
            button = document.getElementById(keyboardAction[x].id)
            classes = button.classList
            if (button.id === "shift") {
                guessWord = !guessWord
                console.log(guessWord)
                if (guessWord == true) {
                    classes.toggle(className, true)
                }
                else {
                    classes.toggle(className, false)
                }
            }
            if (guessWord == true) {
                if (button.id === "enter") {
                    turns = 0
                    guessWord = false
                    gameOver()
                    console.log(guessWord)
                }
                else if (button.id === "backspace") {
                    console.log("Delete")
                }
            }
        })
    }
}

function checkKey(e) {
    if ((e.keyCode >= 65 && e.keyCode <= 90) || (e.keyCode >= 97 && e.keyCode <= 122) && (guessWord == false)) {
        alphabetEvent(e.key)
    }
    // Look up enum for JS and refactor this code so it utilizes it
    button = document.getElementById("shift")
    classes = button.classList;
    if (e.key === "Shift") {
        guessWord = !guessWord;
        console.log(guessWord)
        if (guessWord == true) {
            classes.toggle(className, true);
        }
        else {
            classes.toggle(className, false);
        }
    }
        if (guessWord == true) {
            if (e.key === "Enter") {
                console.log(e.key + " is Enter");
                console.log("This needs to check for the length of the word in future as well")
                guessWord = false
                turns = 0
                gameOver()
                // return e.keyCode;
            }
            else if (e.key === "Backspace") {
                console.log(e.key + " is Backspace");
                // return e.keyCode;
            }
    }
}


// function submitGuess(e) {
    
    // }

    function alphabetEvent(value) {
        if ((turns > 0) && (gameBoard.style.display === "block")) {
            validGuess(value);
            button = document.getElementById(value);
            classes = button.classList;
            classes.toggle(className, true);
        }
    }

function validGuess(guess) {
    guess = guess.toUpperCase()
    if (turns > 0){
        if (guessList.includes(guess)) {
            guessLetter.textContent = `You already guessed the letter ${guess}.  You want to waste a turn???`;
        }
        else {
            guessList.push(guess);
            turns -= 1;
            turnsLeft.textContent = `Turns Left : ${turns}`;
            guessLetter.textContent = `you guessed - ${guess}`;
            letterList.textContent = `${guessList}`;
            
            fetch("/hangman", {
                headers: {
                    "Content-type": "application/json"
                },
                method: "POST",
                body: JSON.stringify(guess)
            })
            gameOver()
        }
    }
}

function gameOver() {
    if (turns == 0) {
        turnsLeft.textContent = `Turns Left : ${turns}`;
        guessLetter.textContent = `GAME OVER D:`;
    }
}

function switchViews() {
    if (gameStart.style.display === "none") {
        gameBoard.style.display = "block"
    }
}

startGame()
checkButton()
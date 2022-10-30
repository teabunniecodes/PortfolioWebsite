const keyboardButton = document.getElementsByClassName("keyboard-button")
const keyboardAction = document.getElementsByClassName("keyboard-action")
const hiddenWord = document.getElementById("hidden-word")
const guessLetter = document.getElementById("letter-guess")
const letterList = document.getElementById("letter-list")
const turnsLeft = document.getElementById("turns-left")
const gameBoard = document.getElementById("game-board")
const gameStart = document.getElementById("game-start")
const gamePlay = document.getElementById("game-play")
let guessList, turns, classes, button
let fullGuess = []
let className = "colored-button"
let guessWord = false
document.onkeyup = checkKey

function getInitialGameState() {
    fetch("/hangman/api/gamestate")
        .then((response) => response.json())
        .then((data) => {dataHandler(data, "?")})
}

function fetchGuess(guess) {
    fetch("/hangman", {
        headers: {
            "Content-type": "application/json"
        },
        method: "POST",
        body: JSON.stringify(guess)
    })
        .then((response) => response.json())
        .then((data) => {dataHandler(data, guess)})
}

function dataHandler(data, guess) {
    guessList = data["guesses"];
    turns = data["turns"];
    word = data["word"];
    win = data["win"]
    updateDOM(guess);
    gameWinOrLose();
}

function startGame() {
    gamePlay.addEventListener ("click", e=> {
        gameStart.style.display = "none";
        switchViews();
        colorMultipleButtons();
    });
}

function colorMultipleButtons() {
    let guesses = guessList.replace(/, /g, "")
    for (let letter of guesses) {
        button = document.getElementById(letter.toLowerCase()).classList
        button.toggle(className, true)
    }
}

function checkButton() {
    for (let x=0; x < keyboardButton.length; x++) {
        keyboardButton[x].addEventListener("click", e => {
            alphabetEvent(keyboardButton[x].id)
            });
        }
    // UI issue still with classList and highlighting the buttons when the game reloads - need to write code to highlight the letters that were already guessed
    for (let x=0; x < keyboardAction.length; x++) {
        keyboardAction[x].addEventListener("click", e => {
            button = document.getElementById(keyboardAction[x].id)
            classes = button.classList
            if (button.id === "shift" && turns > 0 && win === false) {
                guessWord = !guessWord
                if (guessWord == true) {
                    classes.toggle(className, true)
                    hiddenWord.textContent = fullGuess
                }
                else {
                    classes.toggle(className, false)
                    hiddenWord.textContent = `${word}`
                }
            }
            if (guessWord == true) {
                if (button.id === "enter") {
                    turns = 0
                    guessWord = false
                    document.getElementById("shift").classList.toggle(className, false)
                    gameWinOrLose()
                }
                else if (button.id === "backspace") {
                    console.log("Delete")
                    fullGuess.pop();
                }
            }
        })
    }
}

function checkKey(e) {
    if ((e.keyCode >= 65 && e.keyCode <= 90) || (e.keyCode >= 97 && e.keyCode <= 122) && (guessWord === false)) {
        alphabetEvent(e.key)
    }
    // Look up enum for JS and refactor this code so it utilizes it
    button = document.getElementById("shift").classList;
    // classes = button.classList;
    if (e.key === "Shift" && turns > 0 && win === false) {
        guessWord = !guessWord;
        if (guessWord == true) {
            button.toggle(className, true);
            hiddenWord.textContent = "Guess the word"
        }
        else {
            button.toggle(className, false);
            hiddenWord.textContent = `${word}`
            fullGuess.length = 0
        }
    }
        if (guessWord == true) {
            if (e.key === "Enter") {
                // Need to color the buttons of the letters that were typed
                guessWord = false;
                button.toggle(className, false)
                fetchGuess(fullGuess.join(""))
                gameWinOrLose()
                fullGuess.length = 0
            }
            else if (e.key === "Backspace") {
                console.log(e.key + " is Backspace");
                fullGuess.pop();
                hiddenWord.textContent = fullGuess.join(" ")
            }
    }
}

function alphabetEvent(value) {
    if (turns > 0 && gameBoard.style.display === "block" && win === false) {
        if (guessWord == false) {
            validGuess(value);
            button = document.getElementById(value).classList;
            button.toggle(className, true);
        }
        else {
            getFullGuess(value)
        }
    }
}

function validGuess(guess) {
    guess = guess.toUpperCase()
    if (turns > 0) {
        if (guessList.includes(guess)) {
            guessLetter.textContent = `You already guessed the letter ${guess}.  You want to waste a turn???`;
        }
        else {
            fetchGuess(guess)
        }
    }
}

function getFullGuess(guess) {
    fullGuess.push(guess.toUpperCase())
    hiddenWord.textContent = fullGuess.join(" ")
}

function updateDOM(guess) {
    hiddenWord.textContent = `${word}`
    turnsLeft.textContent = `Turns Left : ${turns}`;
    guessLetter.textContent = `You just guessed - ${guess}`; 
    letterList.textContent = `Letters Guessed - ${guessList}`;
}

function gameWinOrLose() {
    colorMultipleButtons()
    if (turns == 0) {
        turnsLeft.textContent = `Turns Left : ${turns}`;
        guessLetter.textContent = `GAME OVER D:`;
        letterList.textContent = `You were so close!`
    }
    else if (win) {
        guessLetter.textContent = `YAY Congrats!`;
        letterList.textContent = `You WON!!!!! :D :D :D`;
    }
}

function switchViews() {
    if (gameStart.style.display === "none") {
        gameBoard.style.display = "block";
    }
    // if (hiddenWord.style.display = "none") {
    //     userFullGuess.style.display = "block"
    // }
    // else if (hiddenWord.style.display = "block") {
    //     userFullGuess.style.display = "none"
    // }
}
    
startGame()
checkButton()
getInitialGameState()
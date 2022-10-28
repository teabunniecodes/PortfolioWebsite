const keyboardButton = document.getElementsByClassName("keyboard-button")
const keyboardAction = document.getElementsByClassName("keyboard-action")
const hiddenWord = document.getElementById("hidden-word")
const guessLetter = document.getElementById("letter-guess")
const letterList = document.getElementById("letter-list")
const turnsLeft = document.getElementById("turns-left")
const gameBoard = document.getElementById("game-board")
const gameStart = document.getElementById("game-start")
const gamePlay = document.getElementById("game-play")
let guessList
let turns
let button = "x"
let classes = "y"
let className = "colored-button"
let guessWord = false
document.onkeyup = checkKey

function getInitialGameState() {
    fetch("/hangman/api/gamestate")
        .then((response) => response.json())
        .then((data) => {dataHandler(data, "?")})
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
            restartGame();
    });
}

function restartGame() {
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
                }
                else {
                    classes.toggle(className, false)
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
        }
        else {
            button.toggle(className, false);
        }
    }
        if (guessWord == true) {
            if (e.key === "Enter") {
                console.log(e.key + " is Enter");
                turns = 0;
                guessWord = false;
                button.toggle(className, false)
                gameWinOrLose()
            }
            else if (e.key === "Backspace") {
                console.log(e.key + " is Backspace");
            }
    }
}

function alphabetEvent(value) {
    if (turns > 0 && gameBoard.style.display === "block" && win === false) {
        validGuess(value);
        button = document.getElementById(value).classList;
        button.toggle(className, true);
    }
}

function validGuess(guess) {
    guess = guess.toUpperCase()
    if (turns > 0) {
        if (guessList.includes(guess)) {
            guessLetter.textContent = `You already guessed the letter ${guess}.  You want to waste a turn???`;
        }
        else {
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
    }
}

function updateDOM(guess) {
    hiddenWord.textContent = `${word}`
    turnsLeft.textContent = `Turns Left : ${turns}`;
    guessLetter.textContent = `You just guessed - ${guess}`; 
    letterList.textContent = `You have already guessed - ${guessList}`;
}

function gameWinOrLose() {
    if (turns == 0) {
        turnsLeft.textContent = `Turns Left : ${turns}`;
        guessLetter.textContent = `GAME OVER D:`;
    }
    else if (win) {
        guessLetter.textContent = `YAY Congrats!`;
    }
}

function switchViews() {
    if (gameStart.style.display === "none") {
        gameBoard.style.display = "block";
    }
}
    
startGame()
checkButton()
getInitialGameState()
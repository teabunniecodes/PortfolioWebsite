const keyboardButton = document.getElementsByClassName("keyboard-button")
const keyboardAction = document.getElementsByClassName("keyboard-action")
const hiddenWord = document.getElementById("hidden-word")
const guessLetter = document.getElementById("letter-guess")
const letterList = document.getElementById("letter-list")
const turnsLeft = document.getElementById("turns-left")
const gameBoard = document.getElementById("game-board")
const gameStart = document.getElementById("game-start")
const gamePlay = document.getElementById("game-play")
const playAgain = document.getElementById("play-again")
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

function resetUserGame() {
    colorMultipleButtons(false)
    fetch("hangman/api/reset_game")
        .then((response) => response.json())
        .then((data) => {dataHandler(data, "?")})
    playAgain.style.display = "none"
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
        colorMultipleButtons(true);
        resetGame()
    });
}

function colorMultipleButtons(boolean) {
    let guesses = guessList.replace(/, /g, "")
    for (let letter of guesses) {
        button = document.getElementById(letter.toLowerCase()).classList
        button.toggle(className, boolean)
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
                    hiddenWord.textContent = "Guess the word"
                }
                else {
                    classes.toggle(className, false)
                    hiddenWord.textContent = `${word}`
                    fullGuess.length = 0
                }
            }
            if (guessWord == true) {
                if (button.id === "enter") {
                    turns = 0
                    guessWord = false
                    document.getElementById("shift").classList.toggle(className, false)
                    if (guessList.length) {
                        fetchGuess(fullGuess.join(""))
                    }
                    console.log(word)
                    gameWinOrLose()
                    fullGuess.length = 0
                }
                else if (button.id === "delete") {
                    fullGuess.pop();
                    hiddenWord.textContent = fullGuess.join(" ")
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
                guessWord = false;
                button.toggle(className, false)
                if (guessList.length) {
                    fetchGuess(fullGuess.join(""))
                }
                gameWinOrLose()
                fullGuess.length = 0
            }
            else if (e.key === "Backspace") {
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
    colorMultipleButtons(true)
    if (turns == 0) {
        turnsLeft.textContent = `Turns Left : ${turns}`;
        guessLetter.textContent = `GAME OVER D:`;
        if (fullGuess) {
            letterList.textContent = `You were so close!`
        }
        else {
            letterList.textContent = `You were so close! You guessed ${fullGuess.join("")}`
        }
    }
    else if (win) {
        guessLetter.textContent = `YAY Congrats!`;
        letterList.textContent = `You WON!!!!! :D :D :D`;
    }
    resetGame()
}

function switchViews() {
    if (gameStart.style.display === "none") {
        gameBoard.style.display = "block";
    }
}

function resetGame() {
    // when the game is over the user will be able to reset the game with a play again button showing up
    // the play again button will have an event that send message to server side to reset their word and turns
    if ((win || turns === 0) && (gameBoard.style.display === "block")) {
        playAgain.style.display = "block"
        playAgain.addEventListener("click", resetUserGame)
    }
}

// fetch("/hangman", {
//     headers: {
//         "Content-type": "application/json"
//     },
//     method: "POST",
//     body: JSON.stringify(guess)
// })
//     .then((response) => response.json())
//     .then((data) => {dataHandler(data, guess)})
    
startGame()
checkButton()
getInitialGameState()
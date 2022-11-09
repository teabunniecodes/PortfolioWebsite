const keyboardButton = document.getElementsByClassName("keyboard-button")
const keyboardAction = document.getElementsByClassName("keyboard-action")
const guesses = document.getElementsByClassName("guesses")
const gameText = document.getElementById("game-text")
let turns = 6
let wordLength = 5
let guessList = []
let gameActive = true
document.onkeyup = checkKey

// This will take the guessList input joined as a string and send it to the server side to check against the valid words
function fetchGuess(guess) {
    fetch("/wordle", {
        headers: {
            "Content-type": "application/json"
        },
        method: "POST",
        body: JSON.stringify(guess.toLowerCase())
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
}

function checkButton() {
    for (let x = 0; x < keyboardButton.length; x++) {
        keyboardButton[x].addEventListener("click", e => {
            validGuess(keyboardButton[x].id)
        });
    }
    for (let x = 0; x < keyboardAction.length; x++) {
        keyboardAction[x].addEventListener("click", e => {
            if (keyboardAction[x].id === "enter") {
                if (guessList.length === wordLength) {
                    fetch(guessList.join("").toUpperCase())
                    guessList.length = 0
                }
                else if (guessList.length) {
                    updateDOM("Guess is too short!!! D:")
                }
                else {
                    updateDOM("Where the heck is your guess??")
                }
            }
            else if (keyboardAction[x].id === "delete") {
                if (guessList.length) {
                    guessList.pop()
                    updateDOM("Second guessing yourself now??")
                }
                if (guessList.length === 0) {
                    guess1.innerText = `Guess 1`
                }
            }
        })
    }
}

function checkKey(e) {
    if ((e.keyCode >= 65 && e.keyCode <= 90) || 
        (e.keyCode >= 97 && e.keyCode <= 122) 
        && gameActive) {
        // alphabetEvent(e.key);
        validGuess(e.key)
    }

    if (e.key === "Enter") {
        // once enter is hit if it is a valid guess it will move to the next guess row
        if (guessList.length === wordLength) {
            fetchGuess(guessList.join("").toUpperCase())
            guessList.length = 0
        }
        // if the length is less that the valid amount of characters the program will yell at you :P
        else if (guessList.length) {
            updateDOM("Your guess is too short!!!")
        }
        // if the length is 0 this enter should not work
        else {
            updateDOM("Where's your guess?")
        }
    }
    else if (e.key === "Backspace") {
        if (guessList.length) {
            guessList.pop();
            updateDOM("Second guessing yourself eh?")
        }
        if (guessList.length === 0) {
            guess1.innerText = `Guess 1`
        }
    }
}

function alphabetEvent(value) {
    // we check the key and add it to the guessList
    if (turns > 0 && gameActive) {
        validGuess(value)
    }
}

// if this is a valid guess this will add a letter to the guessList
function validGuess(guess) {
    if (guessList.length < wordLength && gameActive) {
        guessList.push(guess)
        updateDOM(`You guessed ${guess.toUpperCase()}`)
    }
}

function gameWinOrLose() {
    if (turns === 0) {
        gameActive = false
    }
}

function updateDOM(text) {
    guess1 = document.getElementById("guess-1")
    guess1.innerText = `${guessList.join(" ").toUpperCase()}`
    gameText.innerText = `${text}`
}

checkButton()
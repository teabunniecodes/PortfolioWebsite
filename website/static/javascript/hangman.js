
//TODO WRITE OUT MY PSUEDO CODE D: RAWRRRRRRRRRR

// const words = loadStrings(textdocuments/hangman-wordlist.txt)
const keyboardButton = document.getElementsByClassName("keyboard-button")
const guessLetter = document.getElementById("letter-guess")
const letterList = document.getElementById("letter-list")
const turnsLeft = document.getElementById("turns-left")
const guessList = []
document.onkeyup = checkKey
// document.onkeyup = submitGuess

let turns = 6

function checkButton() {
    for (let x=0; x < keyboardButton.length; x++) {
        keyboardButton[x].addEventListener("click", e => {
            console.log(keyboardButton[x].value);
        });
        // if (e.key === keyboardButton[x]) {
        //     console.log(e.key + " matches the button");
        //     }
    }
}

function checkKey(e) {
    if (turns > 0) {
        if ((e.keyCode >= 65 && e.keyCode <= 90) || (e.keyCode >= 97 && e.keyCode <= 122)) {
            console.log(e.key + " is a letter");
            // let letter = e.key
            validGuess(e.key);
            addGuess(e.key)
        }
    }
    if (turns === 0) {
        gameOver(e.key)
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
        turns -= 1
        turnsLeft.innerHTML = `Turns Left : ${turns}`
        guessList.push(guess.toUpperCase());
        letterList.innerHTML = `${guessList}`;
    }
}


function gameOver(guess) {
    turnsLeft.innerHTML = `Turns Left : ${turns}`;
    guessLetter.innerHTML = `GAME OVER D:`;
}
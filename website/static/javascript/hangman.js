// const words = loadStrings(textdocuments/hangman-wordlist.txt)
const keyboardButton = document.getElementsByClassName("keyboard-button")
const keyboardAction = document.getElementsByClassName("keyboard-action")
const guess = document.getElementById("letter-guess")
document.onkeyup = checkKey

for (let x=0; x < keyboardButton.length; x++) {
    keyboardButton[x].addEventListener("click", e => {
        console.log(keyboardButton[x].value);
    });
    if (e.key === keyboardButton[x]) {
        console.log(e.key + " matches the button");
        }
}


function checkKey(e) {
    // if (letters.includes(e.key)) {
        if (e.key.charCodeAt(0) >= 97 && e.key.charCodeAt(0) <=122) {
            console.log(e.key + " is a letter");
        }
        else {
            console.log(e.key + " Not a letter")
        }
    };
        // }

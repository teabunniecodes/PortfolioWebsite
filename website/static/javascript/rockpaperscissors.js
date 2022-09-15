const btn = document.getElementsByClassName("player-turn")
const buttons = document.getElementById("buttons")
const results = document.getElementById("text-area")
const reset = document.getElementById("play-again")
const turns = ["rock", "paper", "scissor"]

for (let x = 0; x < btn.length; x++) {
    btn[x].addEventListener("click", e=> {
        buttons.style.display = "none"
        switchViews();
        buttonValue(x);
    });
}

function buttonValue(x) {
    let compTurn = Math.floor(Math.random() * turns.length)
    if (btn[x].value === turns[compTurn]) {
        results.innerHTML = (`<p>You both played ${btn[x].value}</p><p>It's a tie!</p>`);
    }
    else if ((btn[x].value === "rock" && compTurn === 2) || (btn[x].value === "paper" && compTurn === 0) || (btn[x].value === "scissor" && compTurn === 1)) {
        results.innerHTML = (`<p>You played ${btn[x].value} and the computer played ${turns[compTurn]}.</p><p>You Won!!!</p>`);
        }
    else {
        results.innerHTML = (`<p>You played ${btn[x].value} and the computer played ${turns[compTurn]}.</p><p>You Lose!!!</p>`);
    }
}

function switchViews() {
    if (buttons.style.display === "none") {
        results.style.display = "block";
        reset.style.display = "block";
    }
}
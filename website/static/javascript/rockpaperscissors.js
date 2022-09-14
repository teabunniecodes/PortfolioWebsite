const btn = document.getElementsByClassName("player-turn")
const body = document.getElementById("text-area")
const turns = ["rock", "paper", "scissor"]

for (let x = 0; x < btn.length; x++) {
    btn[x].addEventListener("click", e=> {
        buttonValue(x);
    });
}

function buttonValue(x) {
    let compTurn = Math.floor(Math.random() * turns.length)
    if (btn[x].value === turns[compTurn]) {
        body.innerHTML = (`<p></p>It's a tie!</p><p>Play again?</p><button class="reset" onClick="window.location.reload();">Yes</button>`);
    }
    // else if ((btn.value === "rock" && turns[compTurn] === "scissor") || (btn.value === "paper" && turns[compTurn] === "rock") || (btn.value === "scissor" && turns[compTurn] === "paper")) {
    else if ((btn[x].value === "rock" && compTurn === 2) || (btn[x].value === "paper" && compTurn === 0) || (btn[x].value === "scissor" && compTurn === 1)) {
        body.innerHTML = (`<p>You played ${btn[x].value} and the computer played ${turns[compTurn]}.</p><p>You Won!!!</p><p>Play again?</p><button class="reset" onClick="window.location.reload();">Yes</button>`);
        // console.log("You played " + btn.value + " and the computer played " + turns[compTurn] + " You Won!!!");
        }
    else {
        body.innerHTML = (`<p>You played ${btn[x].value} and the computer played ${turns[compTurn]}.</p><p>You Lose!!!</p><p>Play again?</p><button class="reset" onClick="window.location.reload();">Yes</button>`);
        // console.log("You played " + btn.value + " and the computer played " + turns[compTurn] + " You Lose!!!");
    }
}

// function playAgain() {
//     body.innerHTML = (`<p>Play again?</p><button class="reset" onClick="window.location.reload();">Yes</button>`);
// }
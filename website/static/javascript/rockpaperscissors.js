const btn = document.getElementsByClassName("player-turn")
const turns = ["rock", "paper", "scissor"]

btn[0].addEventListener("click", e=> {
    console.log(e)
    console.log(e.target)
    buttonValue();
});

btn[1].addEventListener("click", e=> {
    buttonValue();
});

btn[2].addEventListener("click", e=> {
    buttonValue();
});

function buttonValue() {
    let compTurn = Math.floor(Math.random() * turns.length)
    console.log("Player " + btn.value);
    console.log("Comp " + turns[compTurn]);
}
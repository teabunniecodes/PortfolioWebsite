const btn = document.getElementById("mad-libs-button");
const words = document.getElementById("mad-libs-words");
const text = document.getElementById("mad-libs-text");
const reset = document.getElementById("reset")

btn.addEventListener('click', () => {
    words.style.display = "none";
    switchViwes();
    showMadLib();
});

function showMadLib() {
    // body.innerHTML = (`Today I went to the zoo. I saw a(n) ${adj1.value} ${noun1.value} jumping up and down in its tree. He ${verb1.value} ${adv1.value} through the large tunnel that led to its ${adj2.value} ${noun2.value}.`);
    text.innerHTML = (`Today I went to the zoo. I saw a(n) ${adj1.value} ${noun1.value} jumping up and down in its tree. He ${verb1.value} ${adv1.value} through the large tunnel that led to its ${adj2.value} ${noun2.value}. I got some peanuts and passed them through the cage to a gigantic gray ${noun3.value} towering above my head. Feeding that animal made me hungry. I went to get a ${adj3.value} scoop of ice cream. It filled my stomach. Afterwards I had to ${verb2.value} ${adv2.value} to catch our bus. When I got home I ${verb3.value} my mom for a ${adj4.value} day at the zoo.`);
}

function switchViwes() {
    if(words.style.display === "none") {
        text.style.display = "block"
        reset.style.display = "block"
    }
}
const btn = document.getElementById('mad-libs-button')
const body = document.getElementById('mad-libs-text')

btn.addEventListener('click', () => {
    showMadLib();
});

function showMadLib() {
    body.innerHTML = "Today I went to the zoo. I saw a(n) {adjList[0]} {nounList[0]} jumping up and down in its tree. He {verbList[0]} {advList[0]} through the large tunnel that led to its {adjList[1]} {nounList[1]}. I got some peanuts and passed them through the cage to a gigantic gray {nounList[2]} towering above my head. Feeding that animal made me hungry. I went to get a {adjList[2]} scoop of ice cream. It filled my stomach. Afterwards I had to {verbList[1]} {advList[1]} to catch our bus. When I got home I {verbList[2]} my mom for a {adjList[3]} day at the zoo.";
}
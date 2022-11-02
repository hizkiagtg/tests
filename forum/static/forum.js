async function getQuestions() {
    return fetch("{% url 'get_question' %}").then((response) => response.json());
}
async function refreshTask() {
document.getElementById("content").innerHTML = "";
const task = await getTask();
const content = document.getElementById("content");
content.innerHTML = "";
task.forEach((item) => {
    content.innerHTML += `
    <div class="accordion" id="accordionExample">
        <div class="accordion-item">
        <h2 class="accordion-header" id="headingOne">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                ${item.fields.title}
            </button>
        </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                <div class="accordion-body">
                <strong>by ${item.fields.author.username} </strong> 
                <p> ${item.fields.body}</p>
            </div>
        </div>
    </div>
    `;
});
}
function setup() {
    $.ajaxSetup({
        headers: {"X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()}
    });
    getQuestion();
}

async function getQuestion() {
    $.getJSON("json", function(data) {
        var questionHTML = '';
        $.each(data, function (key, task) {
            questionHTML += getCard(task);
        });
        document.getElementById("content").innerHTML = questionHTML;
    })
}

function getCard(task) {
    item = `    
    <div class="accordion" id="accordionExample">
        <div class="accordion-item">
            <h2 class="accordion-header" id="heading${task.pk}">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${task.pk}" aria-expanded="true" aria-controls="collapse${task.pk}">
                    <img src = "https://cdn-icons-png.flaticon.com/512/1179/1179267.png" width = "50" height = "50">
                    <h1>${task.fields.title}</h1>
                </button>
            </h2>
            <div id="collapse${task.pk}" class="accordion-collapse collapse show" aria-labelledby="heading${task.pk}" data-bs-parent="#accordionExample">
                <div class="accordion-body">
                    <strong>Asked by ${task.fields.author}</strong> 
                    <strong>at ${task.fields.created_at} </strong> 
                    <p>${task.fields.body}</p>
                </div>
                <div class ="content-reply">
                    <nav class="navbar navbar-light bg-light">
                    <a class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#modal-reply">Add Your Questions</a>
                    </nav>
                </div>
            </div>
        </div>
    </div>
    `
    return item;
}

async function getReply() {
    $.getJSON("answerJson", function(data) {
        var questionHTML = '';
        $.each(data, function (key, task) {
            questionHTML += getCardReply(task);
        });
        document.getElementById("content-reply").innerHTML = questionHTML;
    })
}

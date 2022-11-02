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
                <button type="button" class="btn btn-info">Respond This Thread</button>
            </div>
        </div>
    </div>
    `
    return item;
}

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

async function getReply() {
    $.getJSON("jsonRep", function(data) {
        var replyHTML = '';
        $.each(data, function (key, task) {
            replyHTML += getReply(task);
        });
        document.getElementById("reply").innerHTML = reply;
    })
}

function getReply(task) {
    item = `    
    <div class="accordion accordion-flush" id="accordionFlushExample">
        <div class="accordion-item">
            <h2 class="accordion-header" id="flush-headingOne">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                Accordion Item #1
            </button>
            </h2>
            <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
            <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the first item's accordion body.</div>
        </div>
    </div>
    `
    return item;
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
                <div id ="content-reply">

                    
                    <a class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#modal-reply">Add Your Answer</a>

                    
                </div>

            </div>
        </div>
    </div>
    `
    return item;
}

function submitNewTask(taskForm) {
    $.post("addQuestion/", $(taskForm).serialize(), function(data){
        document.getElementById("content").innerHTML += getCard(data[0]);
    });
}

function getReply(task) {
    item = `    
    <div class="accordion" id="accordionExample">
        <div class="accordion-item">
            <div id="collapse${task.pk}" class="accordion-collapse collapse show" aria-labelledby="heading${task.pk}" data-bs-parent="#accordionExample">
                <div class="accordion-body">
                    <strong>Asked by ${task.fields.author}</strong> 
                    <strong>at ${task.fields.created_at} </strong> 
                    <p>${task.fields.body}</p>
                </div>
            </div>
        </div>
    </div>
    `
    return item;
}

function submitNewRep(taskForm) {
    $.post("answerJson/", $(taskForm).serialize(), function(data){
        document.getElementById("content-reply").innerHTML += getReply(data[0]);
    });
}

$("#btn_save").click(function(){
    $.post("/user_profile/edit_profile/", {
        name : $('#name').val(),
        username : $('#username').val(),
        age : $('#age').val(),
        gender : $('#gender').val(),
        email : $('email').val(),
        city : $('#city').val(),
        }
        )
})
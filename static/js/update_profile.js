function editBank() {
    $.ajax({
        type: 'POST',
        url: '/profile_user/edit_profile',
        data: $('#edit-bank-form').serialize(),
        
        success: function(response) {
            alert("Profile Successfully Updated!");
        },
        error: function(xhr, status, error) {
            var err = JSON.parse(xhr.responseText);
            alert(err.Message);
        }
    })
}
        //     if (response['success']) {
        //         alert("Profile Successfully Updated!");
        //         document.getElementById("edit-bank-form").reset();
        //     }
        //     else {
        //         alert("Update is Not Successful")
        //         if ("warning" in response) {
        //             alert(response['warning']);
        //         }
        //         else {
        //             var message = "";
        //             for (msg in response['error']) {
        //                 message += response['error'][msg]
        //             }
        //             var newMessage = message.replace(/,/g, "\n");
        //             alert(newMessage)
        //         }
        //     }
        // },


function editReg() {
    $.ajax({
        type: 'POST',
        url: '/profile_user/edit_profile',
        data: $('#edit-reg-form').serialize(),
        
        success: function(response) {
            alert("Profile Successfully Updated!");
        },
        error: function(xhr, status, error) {
            var err = JSON.parse(xhr.responseText);
            alert(err.Message);
        }
    })
}
function bankSignUp() {
  $.ajax({
      type: 'POST',
      url: './bank/',
      data: $('#bank-form').serialize(),
      
      success: function(response) {
          if (response['success']) {
              var message = "You have succesfully signed up!";
              alert(message);
              document.getElementById("bank-form").reset();
              window.location.href = "../login/";
          }
          else {
              if ("warning" in response) {
                  alert(response['warning']);
              }
              else {
                  let req = false;
                  var message = "";
                  for (msg in response['error']) {
                      if (response['error'][msg]=="This field is required.") req = true;
                      else message += (response['error'][msg] + "\n");
                  }
                  if (req) var newMessage = "All fields are required to be filled."
                  else {
                    var newMessage = message.replaceAll(".,", ".\n")
                  }
                  alert(newMessage)
              }
          }
      },
  })
}

function regularSignUp() {
  $.ajax({
      type: 'POST',
      url: './reg/',
      data: $('#reg-form').serialize(),
      
      success: function(response) {
          if (response['success']) {
              var message = "You have succesfully signed up!";
              alert(message);
              document.getElementById("reg-form").reset();
              window.location.href = "../login/";
          }
          else {
              if ("warning" in response) {
                  alert(response['warning']);
              }
              else {
                  let req = false;
                  var message = "";
                  for (msg in response['error']) {
                      if (response['error'][msg]=="This field is required.") req = true;
                      else message += (response['error'][msg] + "\n");
                  }
                  if (req) var newMessage = "All fields are required to be filled."
                  else {
                    var newMessage = message.replaceAll(".,", ".\n")
                    newMessage = newMessage.replace(/@/g, "")
                  }
                  alert(newMessage)
              }
          }
      },
  })
}

let citylist = [
  "Aceh",
  "Sumatera Utara",
  "Sumatera Barat",
  "Riau",
  "Kepulauan Riau",
  "Jambi",
  "Bengkulu",
  "Sumatera Selatan",
  "Kepulauan Bangka Belitung",
  "Lampung",

  "Banten",
  "DKI Jakarta",
  "Jawa Barat",
  "Jawa Tengah",
  "Daerah Istimewa Yogyakarta",
  "Jawa Timur",

  "Bali",
  "Nusa Tenggara Barat",
  "Nusa Tenggara Timur",

  "Kalimantan Barat",
  "Kalimantan Tengah",
  "Kalimantan Timur",
  "Kalimantan Utara",
  "Kalimantan Selatan",

  "Sulawesi Barat",
  "Sulawesi Selatan",
  "Sulawesi Tenggara",
  "Sulawesi Tengah",
  "Gorontalo",
  "Sulawesi Utara",

  "Maluku Utara",
  "Maluku",

  "Papua Barat",
  "Papua",
  "Papua Tengah", 
  "Papua Pegunungan",
  "Papua Selatan"
];

//Sort names in ascending order
let sortedcity = citylist.sort();
var st = '<option disabled selected>--- Pilih Domisili ---</option>'; // variable to store the options
for (var j = 0; j < sortedcity.length; ++j) {
  st += '<option value="' + sortedcity[j] + '" >' + sortedcity[j] + '</option>'; // Storing options in variable
}

document.getElementById("select1").innerHTML = st;
document.getElementById("select2").innerHTML = st;
document.getElementById("domisili-reg").innerHTML = st;
document.getElementById("domisili-bank").innerHTML = st;



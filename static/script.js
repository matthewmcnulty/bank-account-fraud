// JavaScript function to clear the form
function clearForm() {
    var inputs = document.getElementById("prediction_form").getElementsByTagName("input");
    var predictionContainer = document.querySelector(".prediction-container");
    
    // Clear form inputs
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].value = "";
    }
    
    // Clear prediction text
    predictionContainer.textContent = "";
}

// JavaScript function to fill the form with random row data
function fillFormWithRandomRow() {
    // Make an AJAX request to the server to fetch a random row
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_random_row', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);

            // Fill the form with the random row data
            var form = document.getElementById("prediction_form");
            var inputs = form.querySelectorAll("input[name]");

            inputs.forEach(function (input) {
                var name = input.getAttribute("name");
                if (data.hasOwnProperty(name)) {
                    input.value = data[name];
                }
            });
        }
    };
    xhr.send();
}
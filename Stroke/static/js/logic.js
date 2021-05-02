$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        makePredictions();
    });
});

// call Flask API endpoint
function makePredictions() {
    var sex_label = $("#gender").val();
    var age = $("#age").val();
    var married_label = $("#married").val();
    var heart_disease = $("#heart_disease").val();
    var smoke_hist = $("#smoke_hist").val();
    var work_type = $("#work_type").val();
    var hypertension = $("#hypertension").val();
    var avg_glucose_level = $("#avg_glucose_level").val();
    var bmi = $("#bmi").val();
    var residence_label = $("#residence_label").val();

    
    // create the payload
    var payload = {
        "sex_label": sex_label,
        "age": age,
        "married_label": married_label,
        "heart_disease": heart_disease,
        "smoke_hist": smoke_hist,
        "work_type": work_type,
        "hypertension": hypertension,
        "avg_glucose_level": avg_glucose_level,
        "bmi": bmi,
        "residence_label": residence_label
    }
    console.log("age: "+age);
    console.log("bmi: "+bmi);
    console.log("glucose: "+avg_glucose_level);
    console.log("married 1 yes, 0 no: "+married_label);
    console.log("heart disease 1 yes, 0 no: "+heart_disease);
    
    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);

            if (returnedData["prediction"] <= .25) {
                $("#output").text("Very Unlikely "+Math.round((returnedData["prediction"])*1000)/10+"%");
            } else if (returnedData["prediction"] <= .5) {
                $("#output").text("Unlikely "+Math.round((returnedData["prediction"])*1000)/10+"%");
            } else if (returnedData["prediction"] <=.75) {
                $("#output").text("Likely "+Math.round((returnedData["prediction"])*1000)/10+"%");
            }else {
                $("#output").text("Very likely! "+Math.round((returnedData["prediction"])*1000)/10+"%");
            }
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}
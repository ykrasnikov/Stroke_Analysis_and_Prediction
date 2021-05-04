
$(document).ready(function() {
    buildTable(); 
    //Event Listeners
    $("#filter-btn").on("click", function(e) {
        e.preventDefault();
        buildTable();
    });
    $("#filter-clear").on("click", function(e) {
        e.preventDefault();
        resetFilters();
        buildTable();
    });
    $("#form").on("submit", function(e) {
        e.preventDefault();
        buildTable();
    });   
}); 

// id is reference here
function resetFilters() {
    $("#Stroke_choice").val("");

    $("#gender_choice").val("");

    $("#hypertension_choice").val("");

    $("#heart_disease_choice").val("");

    $("#ever_married_choice").val("");    

    $("#smoking_status_choice").val("");

    $("#work_type_choice").val("");

    $("#residence_type_choice").val("");    


}

function buildTable() {
    // live path
    d3.csv("../static/data/healthcare-dataset-stroke-data.csv").then(function(strokeData) {

    // practice path
    // d3.csv("../static/data/healthcare-dataset-stroke-data.csv").then(function(strokeData) {

        var genderFilter = $("#gender_choice").val();
        var hypertensionFilter = ($("#hypertension_choice").val());
        var heartdiseaseFilter = ($("#heart_disease_choice").val());
        var marriedFilter = $("#ever_married_choice").val();
        var workFilter = $("#work_type_choice").val();
        var residenceFilter = $("#residence_type_choice").val();
        var smokingFilter = $("#smoking_status_choice").val();
        var strokeFilter = ($("#Stroke_choice").val());


        // apply filters
        var filteredData = strokeData

        if (genderFilter) {
            filteredData = filteredData.filter(row => (row.gender) === (genderFilter));
            }
        if (hypertensionFilter) {
            filteredData = filteredData.filter(row => (row.hypertension) === (hypertensionFilter));
            } 
        if (heartdiseaseFilter) {
            filteredData = filteredData.filter(row => (row.heart_disease) === (heartdiseaseFilter));
            } 
        if (marriedFilter) {
            filteredData = filteredData.filter(row => (row.ever_married) === (marriedFilter));
            } 
        if (workFilter) {
            filteredData = filteredData.filter(row => (row.work_type) === (workFilter));
            } 
        if (residenceFilter) {
            filteredData = filteredData.filter(row => (row.Residence_type) === (residenceFilter));
            } 
        if (smokingFilter) {
            filteredData = filteredData.filter(row => (row.smoking_status) === (smokingFilter));
            } 
        if (strokeFilter) {
            filteredData = filteredData.filter(row => (row.stroke) === (strokeFilter));
            } 

        buildTableString(filteredData);
    }); 
}

function buildTableString(strokeData) {

    // JQUERY creates an HTML string
    var tbody = $("#table>tbody");
    //clear table
    tbody.empty();

    //destroy datatable
    $("table").DataTable().clear().destroy();

    var datarows = strokeData.map(x => [x["id"], x["gender"], x["age"], x["hypertension"], x["heart_disease"], x["ever_married"] ,x["work_type"],x["Residence_type"],x ["avg_glucose_level"],x["bmi"],x["smoking_status"],x["stroke"]])

    //redraw
    $("#table").DataTable({

        data: datarows,
        "defaultContent": "", 

        "pageLength": 20, 
        dom: 'Bfrtip', //lbfrtip if you want the length changing thing
        buttons: [
            { extend: 'copyHtml5' },
            { extend: 'excelHtml5' },
            { extend: 'csvHtml5' },
            {
                extend: 'pdfHtml5',
                title: function() { return "Stroke Data"; },
                orientation: 'portrait',
                pageSize: 'LETTER',
                text: 'PDF',
                titleAttr: 'PDF'
            }
        ]
    });
}; 


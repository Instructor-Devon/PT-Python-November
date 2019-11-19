$(document).ready(function() {
    $.ajax({
        url: "/dogs"
    }).done(function(res) {
        $("#dogs-table").html(res);
    })
})

$("#dogform").submit(function(e) {
    console.log(e);
    e.preventDefault();
    var formData = $(this).serialize();
    console.log(formData);
    $(this)[0].reset();
    $.ajax({
        url: "/create",
        data: formData,
        method: "POST"
    }).done(function(res) {
        $("#dogs-table").html(res);
    })
    return false;
})
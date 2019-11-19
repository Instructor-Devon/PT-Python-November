// when my page initally loads, i will fetch the dogs


// jquery event for page finished loading
$(document).ready(function() {
    // go fetch the dogs by making a web request!
    $.ajax({
        url: "/dogs"
    }).done(function(res) {
        // when the server responds, html response to the table
        console.log(res);
        $("#dog-body").html(res);
    })
})

// when the form is submitted, send payload to server.  update with lastest dogs from db
$("#dog-form").submit(function(e) {
    e.preventDefault();

    // get the form data, in a serialized format
    var formData = $(this).serialize();

    // reset the form fields
    $(this)[0].reset();

    // send POST request to flask,
    // response will contain updated form body with new dog!
    $.ajax({
        url: "/create",
        method: "POST",
        data: formData
    }).done(function(res) {
        $("#dog-body").html(res);
    })
})
// select    event
$("#button").click(function() {
    // handler
    $.ajax({
        url: "/ajax"
    }).done(function(res) {
        console.log(res);
        $("#content").append(res);
    })
})

$("#test-form").submit(function(e) {
    // prevent normal form behavior
    e.preventDefault();
    var formData = $(this).serialize();
    $.ajax({
        url: "/ajax/post",
        method: "POST",
        data: formData
    }).done(function(res) {
        console.log(res);
        $("#content").append(res);
    })
    console.log(formData);
})
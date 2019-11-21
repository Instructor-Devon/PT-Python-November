$(document).ready(function() {
    $.ajax({
        url: "/dogs"
    }).done(function(res) {
        $("#dogs-table").html(res);
    })
    $.ajax({
        url: "/dogs/json"
    }).done(function(res) {
        console.log(res);
    })
})

$("#dogform").submit(function(e) {
    e.preventDefault();
    var form = this;
    var formData = $(this).serialize();
    $(this)[0].reset();
    $.ajax({
        url: "/create",
        data: formData,
        method: "POST"
    }).done(function(res) {
        if(res.errors) {
            for(var e of res.errors) {
                var el = $(`#${e[0]}`);
                console.log(el, e)
                var txt = `<span class='error'>${ e[1] }</span`
                el.addClass("is-invalid")
                el.parent().prepend(txt); 
            }
        } else {
            $(".form-group").remove(".error");
            for(var inp of form) {
                if($(inp).hasClass("is-invalid")) {
                    $(inp).removeClass("is-invalid");
                }
            }
            $("#dogs-table").html(res);
        }
    })
    return false;
})
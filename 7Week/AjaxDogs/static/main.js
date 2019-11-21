// when my page initally loads, i will fetch the dogs


// jquery event for page finished loading
$(document).ready(function() {
    // go fetch the dogs by making a web request!
    $.ajax({
        url: "/api/dog"
    }).done(function(res) {
        // when the server responds, html response to the table
        for(var dog of res) {
            var tr = $("<tr></tr>");
            var tdName = $(`<td>${ dog.name }</td>`);
            var tdBreed = $(`<td>${ dog.breed }</td>`);
            var tdWeight = $(`<td>${ dog.weight }</td>`);
            $(tr).append(tdName);
            $(tr).append(tdBreed);
            $(tr).append(tdWeight);
            $("#dog-body").append(tr);
        }
    });

    $.ajax({
        url: "/api/test"
    }).done(function(res) {
        // when the server responds, html response to the table
        console.log(res);
    })

})

// when the form is submitted, send payload to server.  update with lastest dogs from db
$("#dog-form").submit(function(e) {
    e.preventDefault();

    // get the form data, in a serialized format
    var formData = $(this).serialize();

    var form = this;
    // reset the form fields
    $(this)[0].reset();

    // send POST request to flask,
    // response will contain updated form body with new dog!
    $.ajax({
        url: "/create",
        method: "POST",
        data: formData
    }).done(function(res) {
        console.log(res)
        if(res.errors) {
            for(var e of res.errors) {
                var el = $(`#${e[0]}`);
                console.log(el, e)
                var txt = `<span class='error'>${ e[1] }</span`
                el.addClass("is-invalid")
                el.parent().prepend(txt); 
            }
        } else {
            for(var ipt of form) {
                if($(ipt).hasClass("is-invalid")) {
                    $(ipt).removeClass("is-invalid");
                }
            }
            $("#dog-body").html(res);
        }
    })
})
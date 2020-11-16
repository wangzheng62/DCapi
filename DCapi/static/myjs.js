function post() {
    $.ajax({
        type: "POST",
        url:$('form').attr('url'),
        data: $('form').serialize(),
        success: function (result,status,xhr) {
            alert('sucess')
        }
    });
}
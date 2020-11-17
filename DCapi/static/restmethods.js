function get() {
    $.ajax({
        type: "GET",
        url:$('form').attr('url'),
        data: $('form').serialize(),
        success: function (result,status,xhr) {
            alert('sucess')
        }
    });
};
function post() {
    $.ajax({
        type: "POST",
        url:$('form').attr('url'),
        data: $('form').serialize(),
        success: function (result,status,xhr) {
            alert('sucess')
        }
    });
};
function put() {
    $.ajax({
        type: "PUT",
        url:$('form').attr('url'),
        data: $('form').serialize(),
        success: function (result,status,xhr) {
            alert('sucess')
        }
    });
};
function del() {
    $.ajax({
        type: "DELETE",
        url:$('form').attr('url'),
        data: $('form').serialize(),
        success: function (result,status,xhr) {
            alert('sucess')
        }
    });
};
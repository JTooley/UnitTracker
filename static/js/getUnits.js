
$(function() {
    updateUnits();
});

function updateUnits() {
    $.ajax({
        url: '/getUnits',
        type: 'GET',
        success: function(res) {
            var unitObj = JSON.parse(res);
            $('#unitList').empty();
            $('#listTemplate').tmpl(unitObj).appendTo('#unitList');
        },
        error: function(error) {
            console.log(error);
        }
    });
}
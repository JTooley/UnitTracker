
function addUnit() {
        console.log("Add Unit")
        $.ajax({
            url: '/addUnit',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                updateUnits();
            },
            error: function(error) {
                console.log(error);
            }
        });
}

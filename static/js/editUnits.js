
function claimUnitConfirm(elem) {
    localStorage.setItem('claimId', $(elem).attr('data-id'));
    $('#claimUnitModal').modal();
}

function releaseUnitConfirm(elem) {
    localStorage.setItem('releaseId', $(elem).attr('data-id'));
    $('#releaseUnitModal').modal();
}

function claimUnit(){
    $.ajax({
        url : '/claimUnit',
        data : {id:localStorage.getItem('claimId'),unitUser:$('#inputUser').val()},
        type : 'POST',
        success: function(res){
            var result = JSON.parse(res);
            if(result.status == 'OK') {
                $('#claimUnitModal').modal('hide');
                updateUnits();
            }
            else {
                alert(result.status);	
            }
        },
        error: function(error){
            console.log(error);
        }
    });
}

function releaseUnit(){
    $.ajax({
        url : '/releaseUnit',
        data : {id:localStorage.getItem('releaseId')},
        type : 'POST',
        success: function(res){
            var result = JSON.parse(res);
            if(result.status == 'OK') {
                $('#releaseUnitModal').modal('hide');
                updateUnits();
            }
            else {
                alert(result.status);	
            }
        },
        error: function(error){
            console.log(error);
        }
    });
}


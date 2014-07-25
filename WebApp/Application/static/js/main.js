
function API(endpoint, auth_token , method, data, callback) {

    if (!(method == "POST" || method == "GET" || method == "PUT" || method == "DELETE")) {
        console.log("Method is not either POST, GET, PUT, or DELETE");
        return
    }
    //Call jQuery ajax
    endpoint = endpoint + '?auth_token=' + auth_token
    $.ajax({
        type: method,
        contentType: "application/json; charset=utf-8",
        url: endpoint,
        data: JSON.stringify(data),
        dataType: "json",
        success: function (msg) {
            console.log("No Error");
            callback(true, msg);
        },
        error: function (err){
            console.log("Error");
            callback(false, err);
        }
    });
}


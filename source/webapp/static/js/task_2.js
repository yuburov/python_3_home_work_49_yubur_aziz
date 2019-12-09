$.ajax({
    url: 'http://localhost:8000/api/login/',
    method: 'post',
    data: JSON.stringify({username: 'admin', password: 'admin'}),
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){console.log(response);},
    error: function(response, status){console.log(response);}

});

localStorage.setItem('api_token', '31b75631780099565f86aca21921daaf5555f683')

$.ajax({
     url: 'http://localhost:8000/api/tasks/',
     method: 'get',
     headers: {'Authorization': 'Token ' + localStorage.getItem('api_token')},
     dataType: 'json',
     success: function(response, status){console.log(response);},
     error: function(response, status){console.log(response);}
});

$.ajax({
     url: 'http://localhost:8000/api/projects/',
     method: 'get',
     headers: {'Authorization': 'Token ' + localStorage.getItem('api_token')},
     dataType: 'json',
     success: function(response, status) {console.log(response);},
     error: function(response, status){console.log(response);}
});

$.ajax({
     url: 'http://localhost:8000/api/projects/',
     method: 'get',
     headers: {'Authorization': 'Token ' + localStorage.getItem('api_token')},
     dataType: 'json',
     success: function(response, status) {for(let i=0;i<response.length;i++)
        {console.log(response[i].tasks)}},
     error: function(response, status){console.log(response);}
});

$.ajax({

    url: 'http://localhost:8000/api/tasks/',
    method: 'post',
    headers: {"Authorization": 'Token ' + localStorage.getItem('apiToken')},
    data: JSON.stringify({summary: 'test555', description: 'test555', status: 1, type: 1, assigned_to: 1, project: 1}),
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){console.log(response);},
    error: function(response, status){console.log(response);}

});

$.ajax({

    url: 'http://localhost:8000/api/tasks/24',
    method: 'delete',
    headers: {"Authorization": 'Token ' + localStorage.getItem('apiToken')},
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){console.log('deleted');},
    error: function(response, status){console.log(response);}
});
$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
    data['results'].forEach(function (val) {
      $('<li>' + val.title + '</li>').appendTo('UL#list_movies');
    });    
  });

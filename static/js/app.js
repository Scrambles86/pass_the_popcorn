/* global $ */


$(document).ready(function () {
  $("#addfilm").hide();

  $("#openAddModal").click(function() {
    $("#addfilm").show();
  });

  $("#closeModal, #closeButton").click(function() {
    $("#addfilm").hide();
  });

  function clearCard() {
    $("#movie-poster").attr("src","");
    $("#movie-title").html("");
    $("#movie-year").html("");
    $("#movie-director").html("");
    $("#movie-starring").html("");
    $("#movie-genre").html("");
  }

  function searchFilmsByTitle(title) {
    let format = title.split(' ').join('+');  // replace spaces with plus
    $.ajax({
      url: `https://www.omdbapi.com/?apikey=ac155d96&s=${format}`,
      dataType: "json"
    }).done(function(resp) {
      if (resp.Search != null) {
        let respSize = resp.Search.length;
        for (let i = 0; i < respSize; i++) {
          if(resp.Search[i].Poster != 'N/A' && resp.Search[i].Type == 'movie') {
            let myHTML = 
            `<div class="col-sm-6">
              <a class="movie-select" href="#" id="${resp.Search[i].imdbID}">
                <img class="movie-image" src="${resp.Search[i].Poster}">
              </a>
            </div>`;
            $("#movies").append(myHTML);
          }
        }
      } else {
        let myHTML =
        `<div class="alert alert-primary" role="alert">
          ${resp.Error}
        </div>`;
        $("#movies").append(myHTML);
      }
    });
  }

  $("#search-movie-new").click(function() {
    $("#movies").html("");
    let searchText = $("#search-text-new").val();
    searchFilmsByTitle(searchText);
  });

  $("#search-text-new").on('keyup', function (e) {
    if (e.keyCode === 13) {
    $("#search-movie-new").click();
    }
  });

  $(document).on("click", ".movie-select", function(e) {
    e.preventDefault();
    $("img.movie-image.movie-selected").removeClass("movie-selected");
    $(this).find(".movie-image").addClass("movie-selected");
    let movieId = this.id;
    
    $.ajax({
      url: `https://www.omdbapi.com/?apikey=ac155d96&i=${movieId}`,
      dataType: "json"
    }).done(function(resp) {
      console.log(resp.Director);
      
      // initialising variables
      let moviePoster = resp.Poster;
      let movieTitle = resp.Title;
      let movieYear = resp.Year;
      let movieDirector = resp.Director;
      let movieActors = resp.Actors;
      let movieGenre = resp.Genre;

      /*

      if (resp.Response === 'True') {
        $("#movie-poster").attr("src",moviePoster);
        $("#movie-title").append(movieTitle);
        $("#movie-year").append(movieYear);
        $("#movie-director").append(movieDirector);
        $("#movie-starring").append(movieActors);
        $("#movie-genre").append(movieGenre);
      } else {
        $(".movie-table").css("display", "none");
        $(".movie-error").css("display", "block");
        $(".movie-error").html(resp.Error);
      }*/
    });
  });

  function searchMovieByTitle(title) {
    let format = title.split(' ').join('+');  // replace spaces with plus
    $.ajax({
      url: `https://www.omdbapi.com/?apikey=ac155d96&t=${format}`,
      dataType: "json"
    }).done(function(resp) {
      console.log(resp);
      $(".movie-error").css("display", "none");
      $(".movie-table").css("display", "block");
      clearCard();

      // initialising variables
      let moviePoster = resp.Poster;
      let movieTitle = resp.Title;
      let movieYear = resp.Year;
      let movieDirector = resp.Director;
      let movieActors = resp.Actors;
      let movieGenre = resp.Genre;


      if (resp.Response === 'True') {
        $("#movie-poster").attr("src",moviePoster);
        $("#movie-title").append(movieTitle);
        $("#movie-year").append(movieYear);
        $("#movie-director").append(movieDirector);
        $("#movie-starring").append(movieActors);
        $("#movie-genre").append(movieGenre);
      } else {
        $(".movie-table").css("display", "none");
        $(".movie-error").css("display", "block");
        $(".movie-error").html(resp.Error);
      }
    });
  }

  // search button onClick
  $("#search-movie").click(function() {
    let searchText = $("#search-text").val();
    searchMovieByTitle(searchText);
  });

});
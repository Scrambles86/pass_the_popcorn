/* global $ */


$(document).ready(function () {
  $("#addfilm").hide();
  $("#movie-thoughts").hide();
  $("editfilm").hide();

  $("#openAddModal").click(function() {
    $("#addfilm").show();
  });

  $("#openEditModal").click(function() {
    $("#editfilm").show();
  });

  $("#closeModal, #closeButton").click(function() {
    $("#addfilm").hide();
  });

  function clearCard() {
    $("#movie_poster").attr("src","");
    $("#movie_title").html("");
    $("#movie_year").html("");
    $("#movie_director").html("");
    $("#movie_starring").html("");
    $("#movie_genre").html("");
    $("movie_score").html("");
  }

  // Adds functionality to search bar, returning movie images related to the user's search
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
        `<div class="col-sm-12">
        <div class="alert alert-primary col" role="alert">
          ${resp.Error}
        </div></div>`;
        $("#movies").append(myHTML);
      }
    });
  }

  $("#search-movie-new").click(function() {
    $("#movies").html("");
    if (!$("#search-text-new").val() || $("#search-text-new").val().length === 0) {
      let myHTML =
        `<div class="col-sm-12">
        <div class="alert alert-primary col" role="alert">
          ERROR: Please enter a movie title
        </div></div>`;
      $("#movies").append(myHTML);
    } else {
      searchFilmsByTitle($("#search-text-new").val());
    }
  });

  // Allows user to use search function with the return key
  $("#search-text-new").on('keyup', function (e) {
    if (e.keyCode === 13) {
    $("#search-movie-new").click();
    }
  });

  // Highlights selected movie poster to user
  $(document).on("click", ".movie-select", function(e) {
    e.preventDefault();
    $("#movie-thoughts").show();
    $("img.movie-image.movie-selected").removeClass("movie-selected");
    $(this).find(".movie-image").addClass("movie-selected");
    let movieId = this.id;
    
    $.ajax({
      url: `https://www.omdbapi.com/?apikey=ac155d96&i=${movieId}`,
      dataType: "json"
    }).done(function(resp) {
      if (resp.Response === 'True') {
        // initialising variables
        let moviePoster = resp.Poster;
        let movieTitle = resp.Title;
        let movieYear = resp.Year;
        let movieDirector = resp.Director;
        let movieActors = resp.Actors;
        let movieGenre = resp.Genre;

        $("#movie_poster").val(moviePoster);
        $("#movie_title").val(movieTitle);
        $("#movie_director").val(movieDirector);
        $("#movie_year").val(movieYear);
        $("#movie_actor").val(movieActors);
        $("#movie_genre").val(movieGenre);
      } else {
        let myHTML =
        `<div class="col-sm-12">
        <div class="alert alert-primary col" role="alert">
          ERROR: This movie doesn't appear to be valid! Try another one
        </div></div>`;
        $("#movies").append(myHTML);
        console.log(resp.Error);
      }
    });
  });

  $("#movie_score").on('keyup change', function (){
    if ($(".movie-selected")[0] && ($("#movie_score").val() || $("#movie_score").val().length !== 0)){
      $('#submit-movie').prop("disabled", false);
    } else {
      $('#submit-movie').prop("disabled", true);
    }
  });
});

// Get the modal
var modal = document.getElementById("infoModal");

// Get the button that opens the modal
var btn = document.getElementById("infoButton");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
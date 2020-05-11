/* global $ */


/*
function closeModal() {
  // if element is present on page and its display value isn't "none"
  if (contentone && contentone.style.display != "none") {
    contentone.style.display = "none";
  }
  if (contenttwo && contenttwo.style.display != "none") {
    contenttwo.style.display = "none";
  }
  if (contentthree && contentthree.style.display != "none") {
    contentthree.style.display = "none";
  }
  formstyle.style.display = "none";
}
*/

/*
function getPoster(poster) {
  fetch(`http://img.omdbapi.com/?i=tt3896198&h=600&apikey=411852b3r=${poster}`)
   .then(response => response.json())
   .then(data => {
     console.log(data)
   })
}
*/

$(document).ready(function () {
  hideModals();

  $("#openAddModal").click(function() {
    $("#addfilm").show();
  });

  $("#openEditModal").click(function() {
    $("#editfilm").show();
  });

  $("#openDeleteModal").click(function() {
    $("#deletefilm").show();
  });

  $("#closeModal").click(function() {
    hideModals();
    console.log("you are clicking close");
  });

  function hideModals() {
    $("#addfilm").hide();
    $("#editfilm").hide();
    $("#deletefilm").hide();
  }

  function clearCard() {
    $("#movie-title").html("");
    $("#movie-year").html("");
    $("#movie-director").html("");
    $("#movie-starring").html("");
    $("#movie-genre").html("");
  }

  function ombdApiGetByTitle(title) {
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

  $("#search-text").on('keyup', function (e) {
    if (e.keyCode === 13) {
    $("#search-movie").click();
    }
  });

  // search button onClick
  $("#search-movie").click(function() {
    let searchText = $("#search-text").val();
    ombdApiGetByTitle(searchText);
  });

});
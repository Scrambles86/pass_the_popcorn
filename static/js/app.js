/* global $ */

// fetch("https://www.omdbapi.com/?i=tt3896198&apikey=ac155d96")
//   .then(res => res.json())
//   .then(data => console.log(data))


// let signup = document.getElementById("signup");
// let addfilm = document.getElementById("addfilm");
// let editfilm = document.getElementById("editfilm");
// let deletefilm = document.getElementById("deletefilm");
let formstyle = document.getElementById("formstyle")


function openCoreModal() {
  formstyle.style.display = "block";
}

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
  if (contentfour && contentfour.style.display != "none") {
    contentfour.style.display = "none";
  }
  formstyle.style.display = "none";
}

function ombdApiGetById(type, movieId) {
   fetch(`https://www.omdbapi.com/?apikey=ac155d96&i=${movieId}`)
    .then(response => response.json())
    .then(data => {
      console.log(data)
    })
}
function getPoster(poster) {
  fetch(`http://img.omdbapi.com/?i=tt3896198&h=600&apikey=411852b3r=${poster}`)
   .then(response => response.json())
   .then(data => {
     console.log(data)
   })
}
function ombdApiGetByActor(actor) {
  fetch(`https://www.omdbapi.com/?apikey=ac155d96&r=${actor}`)
   .then(response => response.json())
   .then(data => {
     console.log(data.Search)
     data.Search.forEach(element => {
       console.log(element.Actor)
     });
   })
}

$(document).ready(function () {
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
      let movieTitle = resp.Title;
      let movieYear = resp.Year;
      let movieDirector = resp.Director;
      let movieActors = resp.Actors;
      let movieGenre = resp.Genre;


      if (resp.Response === 'True') {
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
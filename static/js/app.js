/* global $ */

// fetch("https://www.omdbapi.com/?i=tt3896198&apikey=ac155d96")
//   .then(res => res.json())
//   .then(data => console.log(data))


// let signup = document.getElementById("signup");
// let addfilm = document.getElementById("addfilm");
// let editfilm = document.getElementById("editfilm");
// let deletefilm = document.getElementById("deletefilm");
let formstyle = document.getElementById("formstyle");
let contentone = document.getElementById("contentone");
let contenttwo = document.getElementById("contenttwo");
let contentthree = document.getElementById("contentthree");
let contentfour = document.getElementById("contentfour");


function openSignup() {
  formstyle.style.display = "block";
  contentone.style.display = "block";
}

function openAddModal() {
  formstyle.style.display = "block"; 
  contenttwo.style.display = "block";
}

function openEditModal() {
  formstyle.style.display = "block"; 
  contentthree.style.display = "block";
}

function openDeleteModal() {
  formstyle.style.display = "block"; 
  contentfour.style.display = "block";
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
     console.log(element.Poster)
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

function clearCard() {
  $("#movie-title").html("");
  $("#movie-year").html("");
  $("#movie-director").html("");
  $("#movie-starring").html("");
  $("#movie-genre").html("");
}

function ombdApiGetByTitle(title) {
  $.ajax({
    url: `https://www.omdbapi.com/?apikey=ac155d96&s=${title}`,
    dataType: "json"
  }).done(function(resp) {
    $(".movie-table").css("display", "none");
    clearCard();
    if (resp.Search[0] != null) {
      let movieTitle = resp.Search[0].Title;
      $("#movie-title").append(movieTitle);
    } else {
      $("#movie-title").append("No movies found named " + title);
    }
  });
}

// search button onClick
$("#search-movie").click(function() {
  let searchText = $("#search-text").val();
  ombdApiGetByTitle(searchText);
});


fetch("https://www.omdbapi.com/?i=tt3896198&apikey=ac155d96")
  .then(res => res.json())
  .then(data => console.log(data))


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

//Attempt at search by title. Currently isn't passing argument into fetch
function ombdApiGetByTitle(title) {
   fetch(`https://www.omdbapi.com/?apikey=ac155d96&s=${title}`)
    .then(response => response.json())
    .then(data => {
      console.log(data.Search)
      data.Search.forEach(element => {
        console.log(element.Title)
      });
    })
}
function ombdApiGetById(movieId) {
   fetch(`https://www.omdbapi.com/?apikey=ac155d96&i=${movieId}`)
    .then(response => response.json())
    .then(data => {
      console.log(data)
    })
}
function getPoster(poster) {
  fetch(`http://img.omdbapi.com/?i=tt3896198&h=600&apikey=411852b3=${poster}`)
   .then(response => response.json())
   .then(data => {
     console.log(data)
   })
}
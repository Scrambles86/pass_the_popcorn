fetch("http://www.omdbapi.com/?apikey=ac155d96&")
  .then(res => res.json())
  .then (data => console.log(data))


let signup = document.getElementById("signup");
let addfilm = document.getElementById("addfilm");
let editfilm = document.getElementById("editfilm");
let deletefilm = document.getElementById("deletefilm");


function openSignup() {
  signup.style.display = "block"; 
}

function openAddModal() {
  addfilm.style.display = "block"; 
}

function openEditModal() {
  editfilm.style.display = "block"; 
}

function openDeleteModal() {
  deletefilm.style.display = "block"; 
}

function closeModal() {
  // if element is present on page and its display value isn't "none"
  if (signup && signup.style.display != "none") {
    signup.style.display = "none";
  }
  if (addfilm && addfilm.style.display != "none") {
    addfilm.style.display = "none";
  }
  if (editfilm && editfilm.style.display != "none") {
    editfilm.style.display = "none";
  }
  if (deletefilm && deletefilm.style.display != "none") {
    deletefilm.style.display = "none";
  }
}

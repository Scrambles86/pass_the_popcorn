fetch("http://www.omdbapi.com/?apikey=ac155d96&")
  .then(res => res.json())
  .then (data => console.log(data))


// let signup = document.getElementById("signup");
// let addfilm = document.getElementById("addfilm");
// let editfilm = document.getElementById("editfilm");
// let deletefilm = document.getElementById("deletefilm");
let formstyle = document.getElementsByClassName("formstyle");
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
  // if (signup && signup.style.display != "none") {
  //   signup.style.display = "none";
  // }
  // if (addfilm && addfilm.style.display != "none") {
  //   addfilm.style.display = "none";
  // }
  // if (editfilm && editfilm.style.display != "none") {
  //   editfilm.style.display = "none";
  // }
  // if (deletefilm && deletefilm.style.display != "none") {
  //   deletefilm.style.display = "none";
  // }
  formstyle.style.display = "none";
}

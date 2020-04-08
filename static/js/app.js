var signup = document.getElementById("signup");
var addfilm = document.getElementById("addfilm");
var editfilm = document.getElementById("editfilm");
var deletefilm = document.getElementById("deletefilm");

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

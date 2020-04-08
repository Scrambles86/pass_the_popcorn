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
  if(signup.style.display != "none" || signup.style.display == null) {
    signup.style.display = "none";
  }
  if(addfilm.style.display != "none" || addfilm.style.display == null) {
    addfilm.style.display = "none";
  }
  if(editfilm.style.display != "none" || editfilm.style.display == null) {
    editfilm.style.display = "none";
  }
  if(deletefilm.style.display != "none" || deletefilm.style.display == null) {
    deletefilm.style.display = "none";
  }
}

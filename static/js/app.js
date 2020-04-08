/*function openModal() {
  var modal = document.getElementById("signup");
  modal.style.display = "block"; 
}

function openFilmModal() {
  var filmform = document.getElementById("addfilm");
  filmform.style.display = "block"; 
}

function closebutton() {
  var closebtn = document.getElementById("signup");
  closebtn.style.display = "none"; 
}*/

function showElement (id) {
  var element = document.getElementById(id);
  element.classList.remove("hide");
  element.classList.add("show");
}

function hideElement (id) {
  var element = document.getElementById(id);
  element.classList.remove("show");
  element.classList.add("hide");
}
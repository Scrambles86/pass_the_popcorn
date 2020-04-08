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

function toggleElement(id) {
  var x = document.getElementById(id);
  if (x.style.display == "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
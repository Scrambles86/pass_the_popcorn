function openModal() {
  var modal = document.getElementById("signup");
  modal.style.display = "block"; 
}

function openAddModal() {
  var modal = document.getElementById("addfilm");
  modal.style.display = "block"; 
}

/* Get all elements with class="close" */
var closebtns = document.getElementsByClassName("close");
var i;

/* Loop through the elements, and hide the parent, when clicked on */
for (i = 0; i < closebtns.length; i++) {
  closebtns[i].addEventListener("click", function() {
  this.parentElement.style.display = 'none';
});

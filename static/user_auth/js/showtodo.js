// var warning = document.getElementById('delete_post') ;
var initial = document.getElementById('todo_content') ;
var fedit = document.getElementById('form_edit')
var warning = document.getElementById('delete_post')
warning.style.display = 'none';

function del_func() {
initial.style.display = 'block';
warning.style.display = 'block';
fedit.style.display = 'none'
}
function show_func() {
warning.style.display = 'none';
initial.style.display = 'block';
fedit.style.display = 'none';
}

function edit_func() {
    fedit.style.display = 'block';
    initial.style.display = 'none';
    warning.style.display = 'none' ;
}

window.onclick = function(event) {
    if (event.target == modal) {
      warning.style.display = "none";
    }
  }
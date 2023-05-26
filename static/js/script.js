function showFileName() {
    var input = document.getElementById('image');
    var label = document.querySelector('.custom-file-label');
    var fileName = input.files[0].name;
    label.textContent = "Imagen: " + fileName;
}
  